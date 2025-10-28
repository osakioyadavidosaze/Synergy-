# Deploy Synergy Food to Vercel

## 🚀 Quick Deployment Steps

### 1. Prepare for Deployment
```bash
# Install Vercel CLI
npm i -g vercel

# Login to Vercel
vercel login
```

### 2. Set Environment Variables
In Vercel dashboard or CLI, add:
```
BUSINESS_EMAIL=your-business-email@gmail.com
EMAIL_PASSWORD=your-gmail-app-password
```

### 3. Deploy
```bash
# In your project folder
vercel

# Follow prompts:
# - Link to existing project? No
# - Project name: synergy-food
# - Directory: ./
# - Override settings? No
```

### 4. Custom Domain (Optional)
- Go to Vercel dashboard
- Add your custom domain
- Update DNS records as instructed

## 📁 File Structure for Vercel
```
food-seller-website/
├── index.html          # Main website
├── style.css           # Styling
├── script.js           # Frontend logic
├── vercel.json         # Vercel configuration
├── requirements.txt    # Python dependencies
└── api/
    └── submit-order.py # Serverless function
```

## ⚡ Vercel Features
✅ **Serverless Functions** - No server management
✅ **Global CDN** - Fast worldwide delivery
✅ **Automatic HTTPS** - Secure by default
✅ **Git Integration** - Auto-deploy on push
✅ **Environment Variables** - Secure config storage

## 🔧 Limitations & Solutions

### Database Storage
❌ **No persistent database** on Vercel free tier
✅ **Solution**: Use external services:
- **Airtable** (free, easy setup)
- **Google Sheets API** (free)
- **MongoDB Atlas** (free tier)
- **Supabase** (free PostgreSQL)

### Email Integration
✅ **Gmail SMTP works** with environment variables
✅ **Alternative**: Use email services like:
- **EmailJS** (client-side)
- **SendGrid** (API)
- **Resend** (modern email API)

## 🌐 Live URLs After Deployment
- **Website**: https://synergy-food.vercel.app
- **API**: https://synergy-food.vercel.app/api/submit-order

## 📧 Email Setup
1. **Enable 2FA** on Gmail
2. **Generate App Password**:
   - Google Account → Security → App passwords
   - Select "Mail" and generate password
3. **Add to Vercel environment variables**

## 🔄 Auto-Deployment
- **Connect GitHub repo** to Vercel
- **Auto-deploy** on every push to main branch
- **Preview deployments** for pull requests

Your Synergy Food website will be live globally with professional hosting!