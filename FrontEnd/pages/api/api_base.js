export default function handler(req, res) {
    console.log(req.query.name1);
    const { name1 } = req.query;
    if (!name1) {
      res.status(400).json({ error: 'Invalid project type' });
      return;
    }
    const data = { projectType: name1 };
    res.status(200).json(data);
  }