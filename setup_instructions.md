# Backend Setup Instructions

## 1. Install Dependencies
```bash
pip install flask
```

## 2. Configure Email Settings
Edit `server.py` and update the EMAIL_CONFIG:
```python
EMAIL_CONFIG = {
    'smtp_server': 'smtp.gmail.com',
    'smtp_port': 587,
    'email': 'your-business-email@gmail.com',
    'password': 'your-app-password'  # Generate from Google Account settings
}
```

## 3. Generate Gmail App Password
1. Go to Google Account settings
2. Enable 2-factor authentication
3. Generate an "App Password" for this application
4. Use the app password (not your regular password)

## 4. Run the Server
```bash
python server.py
```

## 5. Access the Website
- Website: http://localhost:5000
- Orders Dashboard: http://localhost:5000/orders

## Features Added:
✅ **Customer Data Storage** - SQLite database stores all orders
✅ **Email Notifications** - Automatic emails to business owner
✅ **Customer Confirmations** - Optional email receipts to customers
✅ **Order Dashboard** - View all orders at /orders
✅ **Order Tracking** - Unique order numbers generated
✅ **Real-time Status** - Loading states and error handling

## Database Schema:
- Order number, customer details, items, totals
- Timestamps, delivery options, payment methods
- Order status tracking (pending, confirmed, delivered)

## Email Templates:
- Business notification with full order details
- Customer confirmation with order summary
- Professional HTML formatting