export default async function handler(req, res) {
  // Set CORS headers
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  res.setHeader('Content-Type', 'application/json');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ success: false, error: 'Method not allowed' });
  }

  try {
    const data = req.body;
    
    if (!data || !data.name || !data.phone) {
      return res.status(400).json({ success: false, error: 'Missing required fields' });
    }
    
    const orderNumber = `SYN${Date.now().toString().slice(-8)}`;
    
    // For now, just return success - you can add email/database logic later
    return res.status(200).json({
      success: true,
      order_number: orderNumber
    });
    
  } catch (error) {
    return res.status(500).json({
      success: false,
      error: 'Server error occurred'
    });
  }
}
