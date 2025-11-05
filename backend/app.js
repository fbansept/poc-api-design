const express = require('express');
const app = express();
const port = 3000;

// Liste de tâches
const todoList = [
  { id: 1, task: "Faire les courses", completed: false },
  { id: 2, task: "Aller à la salle de sport", completed: true },
  { id: 3, task: "Lire un livre", completed: false },
  { id: 4, task: "Envoyer un email", completed: false }
];

app.get('/todo/list', (req, res) => {
  res.json(todoList); // Envoyer la liste de tâches en JSON
});

app.listen(port, () => {
  console.log(`Serveur démarré sur http://localhost:${port}`);
});