#!/usr/bin/env python3
"""
Price Monitor - Web Dashboard (PWA)
Professional web interface for price monitoring
"""

from flask import Flask, render_template, request, redirect, url_for, session, jsonify, flash
from functools import wraps
import json
import os
from datetime import datetime
import hashlib
import secrets
import requests
from bs4 import BeautifulSoup
import re
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import schedule
import threading
import time

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', secrets.token_hex(32))

# Configuration
GMAIL_EMAIL = os.environ.get('GMAIL_EMAIL', '')
GMAIL_PASSWORD = os.environ.get('GMAIL_PASSWORD', '')
USERNAME = os.environ.get('DASHBOARD_USERNAME', 'ali')
PASSWORD_HASH = os.environ.get('DASHBOARD_PASSWORD_HASH', hashlib.sha256('password123'.encode()).hexdigest())

DATA_FILE = 'data/products.json'

# Ensure data directory exists
os.makedirs('data', exist_ok=True)

def load_data():
    """Load products data"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    else:
        return {
            "email": {
                "sender_email": GMAIL_EMAIL,
                "recipient_email": GMAIL_EMAIL
            },
            "products": [],
            "last_run": {
                "timestamp": None,
                "products_checked": 0,
                "deals_found": 0,
                "email_sent": False
            },
            "statistics": {
                "total_savings": 0,
                "total_deals": 0
            }
        }

def save_data(data):
    """Save products data"""
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def login_required(f):
    """Decorator for routes requiring login"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login page"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        
        if username == USERNAME and password_hash == PASSWORD_HASH:
            session['logged_in'] = True
            session['username'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials!', 'error')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    """Logout"""
    session.clear()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('login'))

@app.route('/')
@login_required
def dashboard():
    """Main dashboard"""
    data = load_data()
    
    # Calculate statistics
    total_products = len(data['products'])
    active_products = len([p for p in data['products'] if p.get('enabled', True)])
    deals_found = len([p for p in data['products'] if p.get('current_price') and p['current_price'] <= p['target_price']])
    
    total_savings = 0
    for product in data['products']:
        if product.get('current_price') and product['current_price'] <= product['target_price']:
            total_savings += (product['target_price'] - product['current_price'])
    
    stats = {
        'total_products': total_products,
        'active_products': active_products,
        'deals_found': deals_found,
        'total_savings': total_savings,
        'last_run': data['last_run']
    }
    
    return render_template('dashboard.html', 
                         products=data['products'], 
                         stats=stats,
                         username=session.get('username'))

@app.route('/products')
@login_required
def products():
    """Product management page"""
    data = load_data()
    return render_template('products.html', 
                         products=data['products'],
                         username=session.get('username'))

@app.route('/products/add', methods=['POST'])
@login_required
def add_product():
    """Add new product"""
    data = load_data()
    
    name = request.form.get('name')
    url = request.form.get('url')
    target_price = float(request.form.get('target_price'))
    
    if not url.startswith('http'):
        flash('URL must start with http:// or https://', 'error')
        return redirect(url_for('products'))
    
    new_product = {
        "id": len(data['products']) + 1,
        "name": name,
        "url": url,
        "target_price": target_price,
        "current_price": None,
        "last_check": None,
        "enabled": True,
        "alert_sent": False,
        "created_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    data['products'].append(new_product)
    save_data(data)
    
    flash(f'Product "{name}" added successfully!', 'success')
    return redirect(url_for('products'))

@app.route('/products/edit/<int:product_id>', methods=['GET', 'POST'])
@login_required
def edit_product(product_id):
    """Edit product"""
    data = load_data()
    product = next((p for p in data['products'] if p['id'] == product_id), None)
    
    if not product:
        flash('Product not found!', 'error')
        return redirect(url_for('products'))
    
    if request.method == 'POST':
        product['name'] = request.form.get('name')
        product['url'] = request.form.get('url')
        product['target_price'] = float(request.form.get('target_price'))
        
        save_data(data)
        flash(f'Product "{product["name"]}" updated!', 'success')
        return redirect(url_for('products'))
    
    return render_template('edit_product.html', product=product, username=session.get('username'))

@app.route('/products/delete/<int:product_id>', methods=['POST'])
@login_required
def delete_product(product_id):
    """Delete product"""
    data = load_data()
    data['products'] = [p for p in data['products'] if p['id'] != product_id]
    
    # Renumber IDs
    for i, product in enumerate(data['products'], 1):
        product['id'] = i
    
    save_data(data)
    flash('Product deleted successfully!', 'success')
    return redirect(url_for('products'))

@app.route('/products/toggle/<int:product_id>', methods=['POST'])
@login_required
def toggle_product(product_id):
    """Enable/disable product"""
    data = load_data()
    product = next((p for p in data['products'] if p['id'] == product_id), None)
    
    if product:
        product['enabled'] = not product.get('enabled', True)
        save_data(data)
        status = "enabled" if product['enabled'] else "disabled"
        flash(f'Product {status}!', 'success')
    
    return redirect(url_for('products'))

@app.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    """Settings page"""
    data = load_data()
    
    if request.method == 'POST':
        data['email']['sender_email'] = request.form.get('email')
        data['email']['recipient_email'] = request.form.get('email')
        
        # Optional: update password
        gmail_password = request.form.get('gmail_password')
        if gmail_password:
            # Save to environment or config (in production, use proper secrets management)
            pass
        
        save_data(data)
        flash('Settings updated!', 'success')
    
    return render_template('settings.html', 
                         email=data['email'],
                         username=session.get('username'))

@app.route('/check-now', methods=['POST'])
@login_required
def check_now():
    """Trigger manual price check"""
    threading.Thread(target=check_all_prices, daemon=True).start()
    flash('Price check started! Results will appear shortly.', 'info')
    return redirect(url_for('dashboard'))

@app.route('/api/stats')
@login_required
def api_stats():
    """API endpoint for statistics"""
    data = load_data()
    
    total_products = len(data['products'])
    deals_found = len([p for p in data['products'] if p.get('current_price') and p['current_price'] <= p['target_price']])
    
    return jsonify({
        'total_products': total_products,
        'deals_found': deals_found,
        'last_run': data['last_run']
    })

def check_price(url):
    """Check price for a URL"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=15)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Try various price selectors
        price_selectors = [
            ('class', 'a-price-whole'),
            ('class', 'a-offscreen'),
            ('class', 'value'),
            ('class', 'price'),
        ]
        
        for attr_name, attr_value in price_selectors:
            elements = soup.find_all(attrs={attr_name: attr_value})
            for element in elements:
                text = element.get_text().strip().replace('$', '').replace(',', '')
                price_match = re.search(r'(\d{1,5}(?:\.\d{2})?)', text)
                if price_match:
                    price = float(price_match.group(1))
                    if 1 <= price <= 100000:
                        return price
        
        return None
    except:
        return None

def send_email_alert(alerts):
    """Send email alert"""
    try:
        data = load_data()
        recipient = data['email']['recipient_email']
        
        msg = MIMEMultipart()
        msg['From'] = GMAIL_EMAIL
        msg['To'] = recipient
        msg['Subject'] = f"🎯 Price Alert! {len(alerts)} Deal(s) Found!"
        
        body = "Price Monitor found deals!\n\n"
        for alert in alerts:
            body += f"📦 {alert['name']}\n"
            body += f"   Target: ${alert['target_price']:.2f}\n"
            body += f"   Current: ${alert['current_price']:.2f}\n"
            body += f"   Savings: ${alert['target_price'] - alert['current_price']:.2f}\n\n"
        
        msg.attach(MIMEText(body, 'plain'))
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(GMAIL_EMAIL, GMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
        
        return True
    except:
        return False

def check_all_prices():
    """Check all product prices"""
    data = load_data()
    alerts = []
    
    for product in data['products']:
        if not product.get('enabled', True):
            continue
        
        price = check_price(product['url'])
        
        if price:
            product['current_price'] = price
            product['last_check'] = datetime.now().strftime('%m/%d %H:%M')
            
            if price <= product['target_price']:
                product['alert_sent'] = True
                alerts.append({
                    'name': product['name'],
                    'target_price': product['target_price'],
                    'current_price': price
                })
    
    # Update last run
    data['last_run'] = {
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'products_checked': len([p for p in data['products'] if p.get('enabled', True)]),
        'deals_found': len(alerts),
        'email_sent': False
    }
    
    if alerts:
        email_sent = send_email_alert(alerts)
        data['last_run']['email_sent'] = email_sent
    
    save_data(data)

def schedule_checker():
    """Run scheduled price checks"""
    schedule.every().day.at("12:00").do(check_all_prices)
    
    while True:
        schedule.run_pending()
        time.sleep(60)

# Start scheduler in background
threading.Thread(target=schedule_checker, daemon=True).start()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
