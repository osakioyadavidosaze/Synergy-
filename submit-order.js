export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  try {
    const data = req.body;
    const orderNumber = `SYN${Date.now().toString().slice(-8)}`;
    
    // Send email using a service like EmailJS or store in external DB
    // For now, just return success with order number
    
    res.status(200).json({
      success: true,
      order_number: orderNumber,
      message: 'Order received successfully'
    });
    
  } catch (error) {
    res.status(500).json({
      success: false,
      error: error.message
    });
  }
}