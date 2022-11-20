const express = require('express');
const app = express();
const port = 3000;

app.post('/login', (req, res) => {
  const { username, password } = req.body;
  if (auth(username, password)) {
    res.redirect(req.query.redirect_url ? req.query.redirect_url : '/');
  } else {
    res.render('login', { error: 'Incorrect Credentials Supplied' });
  }
});

app.listen(port, () => {
  console.log(`Listening on http://localhost:${port}`);
});

// Not vulnerable
const express = require('express');
const app = express();
const port = 3000;

app.post('/login', (req, res) => {
  const { username, password } = req.body;
  if (auth(username, password)) {
    const redirect = req.query.redirect_url ? req.query.redirect_url : '';
    res.redirect('https://papertown.com/' + redirect);
  } else {
    res.render('login', { error: 'Incorrect Credentials Supplied' });
  }
});

app.listen(port, () => {
  console.log(`Listening on http://localhost:${port}`);
});

// Not vulnerable

const express = require('express');
const app = express();
const port = 3000;

app.post('/login', (req, res) => {
  const { username, password } = req.body;
  if (auth(username, password)) {
    const redirect = req.query.redirect_url ? req.query.redirect_url : '';
    res.redirect('https://papertown.com/' + redirect);
  } else {
    res.render('login', { error: 'Incorrect Credentials Supplied' });
  }
});

app.listen(port, () => {
  console.log(`Listening on http://localhost:${port}`);
});