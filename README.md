═══════════════════════════════════════════════════════════
  PRICE MONITOR WEB APP - COMPLETE SETUP GUIDE
  Professional Dashboard with PWA (iPhone App Support!)
═══════════════════════════════════════════════════════════

🎉 CONGRATULATIONS! You now have a professional web dashboard!

✅ Features:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ Beautiful modern dashboard
✓ Product management (Add/Edit/Delete)
✓ Automatic price checking (daily 12 PM)
✓ Email alerts
✓ Mobile responsive
✓ PWA - Install as iPhone/Android app!
✓ Secure login system
✓ Cloud-based (100%)
✓ Professional design

═══════════════════════════════════════════════════════════
STEP 1: UPLOAD TO GITHUB
═══════════════════════════════════════════════════════════

A. CREATE NEW REPOSITORY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Go to: https://github.com/new
2. Repository name: price-monitor-web
3. Description: Professional Price Monitoring Dashboard
4. Visibility: Private (recommended for security)
5. Click "Create repository"

B. UPLOAD FILES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. In your new repo, click "uploading an existing file"
2. Upload ALL files from the web-app folder:
   ✓ app.py
   ✓ requirements.txt
   ✓ Procfile
   ✓ railway.json
   ✓ runtime.txt
   ✓ templates/ (folder with all HTML files)
   ✓ static/ (folder with manifest, service-worker)
   ✓ data/ (folder with products.json)

3. Click "Commit changes"

Your GitHub repo structure should look like:
```
price-monitor-web/
├── app.py
├── requirements.txt
├── Procfile
├── railway.json
├── runtime.txt
├── templates/
│   ├── login.html
│   ├── dashboard.html
│   ├── products.html
│   ├── edit_product.html
│   └── settings.html
├── static/
│   ├── manifest.json
│   ├── service-worker.js
│   └── icons/ (will add icons later)
└── data/
    └── products.json
```

═══════════════════════════════════════════════════════════
STEP 2: DEPLOY TO RAILWAY
═══════════════════════════════════════════════════════════

A. CREATE NEW PROJECT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Go to: https://railway.app/
2. Click "New Project"
3. Select "Deploy from GitHub repo"
4. Choose "price-monitor-web"
5. Railway will start building!

B. CONFIGURE ENVIRONMENT VARIABLES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CRITICAL: Set these in Railway dashboard!

1. Click your project
2. Go to "Variables" tab
3. Add these variables:

   Variable: SECRET_KEY
   Value: [Copy this random key]
   09a8f7b6c5d4e3f2a1b0c9d8e7f6a5b4c3d2e1f0a9b8c7d6e5f4a3b2c1d0

   Variable: GMAIL_EMAIL
   Value: hooya911@gmail.com

   Variable: GMAIL_PASSWORD
   Value: smhj utlt ekrd hcnw

   Variable: DASHBOARD_USERNAME
   Value: ali

   Variable: DASHBOARD_PASSWORD_HASH
   Value: ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f
   (This is the hash for password: password123)

4. Click "Add" for each variable
5. Railway will automatically redeploy

═══════════════════════════════════════════════════════════
STEP 3: ACCESS YOUR WEB DASHBOARD
═══════════════════════════════════════════════════════════

A. GET YOUR URL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. In Railway dashboard, click "Deployments"
2. Click the latest successful deployment
3. Look for the domain, something like:
   https://price-monitor-web-production.up.railway.app

B. LOGIN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Open the URL
2. Login with:
   Username: ali
   Password: password123

3. You're in! 🎉

═══════════════════════════════════════════════════════════
STEP 4: INSTALL AS iPHONE APP (PWA)
═══════════════════════════════════════════════════════════

ON iPHONE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Open Safari (must use Safari, not Chrome!)
2. Go to your Railway URL
3. Login to your dashboard
4. Tap the "Share" button (box with arrow)
5. Scroll down and tap "Add to Home Screen"
6. Name it: "Price Monitor"
7. Tap "Add"

NOW: Icon appears on your iPhone home screen! 📱

8. Tap the icon
9. Opens like a real native app!
10. No browser bars, full screen! ✨

ON ANDROID:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Open Chrome
2. Go to your Railway URL
3. Login
4. Chrome will show "Add to Home Screen" banner
5. Tap "Install"
6. Done!

═══════════════════════════════════════════════════════════
STEP 5: USING YOUR DASHBOARD
═══════════════════════════════════════════════════════════

DASHBOARD PAGE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• View statistics (total products, deals, savings)
• See last price check status
• Quick add new product
• View recent products
• Manual "Check Now" button

PRODUCTS PAGE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• Add new products
• Edit existing products (✏️ button)
• Delete products (🗑️ button)
• Enable/disable products (⏸️ button)
• View all product details

SETTINGS PAGE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• Configure email address
• View schedule information
• See app version and info

═══════════════════════════════════════════════════════════
HOW IT WORKS
═══════════════════════════════════════════════════════════

AUTOMATIC CHECKING:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Every day at 12:00 PM EST:
1. Railway wakes up
2. Checks all enabled products
3. Updates prices in database
4. If any deals found (price ≤ target):
   → Sends email alert
5. Updates dashboard statistics
6. Goes back to sleep

ACCESS FROM ANYWHERE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• At home: Desktop browser
• At work: Work computer
• On the go: iPhone/Android app
• Traveling: Any device with internet
• Same data everywhere! ☁️

═══════════════════════════════════════════════════════════
SECURITY FEATURES
═══════════════════════════════════════════════════════════

✅ HTTPS encryption (Railway provides free SSL)
✅ Password protected login
✅ Session management (auto-logout)
✅ Hashed passwords (not stored in plain text)
✅ Environment variables for secrets
✅ No desktop files (100% cloud)

═══════════════════════════════════════════════════════════
CUSTOMIZATION
═══════════════════════════════════════════════════════════

CHANGE LOGIN PASSWORD:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Go to: https://www.browserling.com/tools/sha256
2. Enter your desired password
3. Copy the hash
4. In Railway → Variables → DASHBOARD_PASSWORD_HASH
5. Paste the new hash
6. Railway redeploys
7. Login with new password!

ADD CUSTOM DOMAIN (Optional):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
If you own a domain (like ali-price-monitor.com):
1. Railway Settings → Domains
2. Add custom domain
3. Update DNS records
4. Get branded URL!

═══════════════════════════════════════════════════════════
FOR YOUR RESUME / PORTFOLIO
═══════════════════════════════════════════════════════════

You can showcase this as:

PROJECT: Price Monitor - Full-Stack Web Application
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Description:
Professional e-commerce price monitoring system with automated
tracking, email notifications, and mobile-responsive dashboard.

Technologies:
• Backend: Python, Flask, RESTful API
• Frontend: HTML5, Bootstrap 5, JavaScript
• Database: JSON-based data persistence
• Cloud: Railway PaaS, HTTPS/SSL
• Features: PWA, Service Workers, Responsive Design
• Integration: SMTP email, Web scraping, BeautifulSoup
• Security: Session management, password hashing

Key Features:
• Progressive Web App (installable on iOS/Android)
• Real-time price monitoring with web scraping
• Automated daily price checks via scheduler
• Email notification system
• Full CRUD operations for product management
• Mobile-first responsive design
• Cloud-based deployment
• Secure authentication system

Live Demo: [Your Railway URL]
GitHub: https://github.com/[your-username]/price-monitor-web

═══════════════════════════════════════════════════════════
COST
═══════════════════════════════════════════════════════════

Railway Pricing:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ You pay: $5/month (Hobby Plan)
✅ Includes:
   • Telegram bot (~$1-2/month)
   • Price Monitor Web (~$2-3/month)
   • Total usage: ~$3-4/month
✅ Still under $5 limit!

NO ADDITIONAL COST! 🎉

═══════════════════════════════════════════════════════════
TROUBLESHOOTING
═══════════════════════════════════════════════════════════

PROBLEM: Can't login
SOLUTION: Username is "ali", password is "password123"

PROBLEM: Railway build failed
SOLUTION: Check all files uploaded correctly, verify Procfile exists

PROBLEM: No prices showing
SOLUTION: Click "Check Prices Now" button to trigger manual check

PROBLEM: Not receiving emails
SOLUTION: Verify GMAIL_EMAIL and GMAIL_PASSWORD in Railway variables

PROBLEM: iPhone app doesn't install
SOLUTION: Must use Safari browser, not Chrome. Tap Share → Add to Home Screen

═══════════════════════════════════════════════════════════
NEXT STEPS
═══════════════════════════════════════════════════════════

1. ✅ Upload files to GitHub
2. ✅ Deploy to Railway
3. ✅ Set environment variables
4. ✅ Access your dashboard
5. ✅ Install as iPhone app
6. ✅ Add your products
7. ✅ Test price checking
8. ✅ Show to friends! 🎉

═══════════════════════════════════════════════════════════

Enjoy your professional price monitoring dashboard!
Access it anywhere, anytime, from any device! 🚀

═══════════════════════════════════════════════════════════
