from flask import Flask, request, jsonify, render_template_string
import smtplib
import sqlite3
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import json

app = Flask(__name__)

# Database setup
def init_db():
    conn = sqlite3.connect('orders.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS orders
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  order_number TEXT,
                  customer_name TEXT,
                  phone TEXT,
                  email TEXT,
                  address TEXT,
                  items TEXT,
                  total REAL,
                  delivery_option TEXT,
                  payment_method TEXT,
                  order_date TEXT,
                  status TEXT DEFAULT 'pending')''')
    conn.commit()
    conn.close()

# Email configuration
EMAIL_CONFIG = {
    'smtp_server': 'smtp.gmail.com',
    'smtp_port': 587,
    'email': 'your-email@gmail.com',  # Replace with your email
    'password': 'your-app-password'   # Replace with your app password
}

def send_email(to_email, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_CONFIG['email']
        msg['To'] = to_email
        msg['Subject'] = subject
        
        msg.attach(MIMEText(body, 'html'))
        
        server = smtplib.SMTP(EMAIL_CONFIG['smtp_server'], EMAIL_CONFIG['smtp_port'])
        server.starttls()
        server.login(EMAIL_CONFIG['email'], EMAIL_CONFIG['password'])
        server.send_message(msg)
        server.quit()
        return True
    except Exception as e:
        print(f"Email error: {e}")
        return False

@app.route('/')
def index():
    return render_template_string(open('index.html').read())

@app.route('/submit-order', methods=['POST'])
def submit_order():
    try:
        data = request.json
        
        # Generate order number
        order_number = f"SYN{datetime.now().strftime('%Y%m%d%H%M%S')}"
        
        # Store in database
        conn = sqlite3.connect('orders.db')
        c = conn.cursor()
        c.execute('''INSERT INTO orders 
                     (order_number, customer_name, phone, email, address, items, total, 
                      delivery_option, payment_method, order_date)
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                  (order_number, data['name'], data['phone'], data.get('email', ''),
                   data['address'], json.dumps(data['items']), data['total'],
                   data['delivery'], data['payment'], datetime.now().isoformat()))
        conn.commit()
        conn.close()
        
        # Send email to business owner
        items_html = '<br>'.join([f"{item['product']} x{item['quantity']}kg - ₦{item['total']:,}" 
                                 for item in data['items']])
        
        business_email_body = f"""
        <h2>🍠 New Order - Synergy Food</h2>
        <p><strong>Order #:</strong> {order_number}</p>
        <p><strong>Customer:</strong> {data['name']}</p>
        <p><strong>Phone:</strong> {data['phone']}</p>
        <p><strong>Address:</strong> {data['address']}</p>
        <p><strong>Delivery:</strong> {data['delivery']}</p>
        <p><strong>Payment:</strong> {data['payment']}</p>
        
        <h3>Items Ordered:</h3>
        {items_html}
        
        <p><strong>Total:</strong> ₦{data['total']:,}</p>
        <p><strong>Order Time:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        """
        
        send_email(EMAIL_CONFIG['email'], f"New Order #{order_number}", business_email_body)
        
        # Send confirmation email to customer (if email provided)
        if data.get('email'):
            customer_email_body = f"""
            <h2>🎉 Order Confirmed - Synergy Food</h2>
            <p>Dear {data['name']},</p>
            <p>Thank you for your order! Here are the details:</p>
            
            <p><strong>Order #:</strong> {order_number}</p>
            <p><strong>Items:</strong><br>{items_html}</p>
            <p><strong>Total:</strong> ₦{data['total']:,}</p>
            <p><strong>Delivery:</strong> {data['delivery']}</p>
            
            <p>📞 We'll call you at {data['phone']} within 30 minutes to confirm delivery.</p>
            <p>🚚 Expected delivery: 2-4 hours</p>
            
            <p>Thank you for choosing Synergy Food! 🍠</p>
            """
            send_email(data['email'], f"Order Confirmation #{order_number}", customer_email_body)
        
        return jsonify({'success': True, 'order_number': order_number})
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/orders')
def view_orders():
    conn = sqlite3.connect('orders.db')
    c = conn.cursor()
    c.execute('SELECT * FROM orders ORDER BY order_date DESC')
    orders = c.fetchall()
    conn.close()
    
    orders_html = """
    <h1>📊 Synergy Food Orders</h1>
    <table border="1" style="width:100%; border-collapse:collapse;">
    <tr><th>Order #</th><th>Customer</th><th>Phone</th><th>Items</th><th>Total</th><th>Date</th><th>Status</th></tr>
    """
    
    for order in orders:
        items = json.loads(order[6])
        items_str = ', '.join([f"{item['product']} x{item['quantity']}" for item in items])
        orders_html += f"""
        <tr>
            <td>{order[1]}</td>
            <td>{order[2]}</td>
            <td>{order[3]}</td>
            <td>{items_str}</td>
            <td>₦{order[7]:,.0f}</td>
            <td>{order[10][:16]}</td>
            <td>{order[11]}</td>
        </tr>
        """
    
    orders_html += "</table>"
    return orders_html

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)