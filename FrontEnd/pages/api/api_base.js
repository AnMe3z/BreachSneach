export default function handler(req, res) {
    console.log(req.query.name1);
    const array = [
      { name: 'John', percentage: 20 },
      { name: 'Mary', percentage: 30 },
      { name: 'David', percentage: 15 },
      { name: 'Lisa', percentage: 10 },
      { name: 'Michael', percentage: 25 },
    ];
    array[0].name = req.query
    const { name1 } = req.query;//imeto na poleto ot frontenda
    if (!name1) {
      res.status(400).json({ error: 'Invalid project type' });
      return;
    }
    const data = { projectType: name1 };
    res.status(200).json(array);
  }