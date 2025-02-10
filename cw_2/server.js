const express = require('express');
const app = express();

// Сервер порты
const PORT = 3000;

// Басты бетке жауап беру
app.get('/', (req, res) => {
    res.send('Сәлем, бұл Node.js сервері жұмыс істеп тұр!');
});

// Серверді іске қосу
app.listen(PORT, () => {
    console.log(`Сервер http://localhost:${PORT} адресінде іске қосылды`);
});
