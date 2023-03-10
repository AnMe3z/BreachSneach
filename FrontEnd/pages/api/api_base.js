export default function handler(req, res) {
    const { name } = req.query;
    if (!name) {
      res.status(400).json({ error: 'Name is required' });
      return;
    }
    res.status(200).json({ message: `Hello, ${name}!` });
  }
  