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


const app = require("express")();

app.get('/some/path', function(req, res) {
  // BAD: a request parameter is incorporated without validation into a URL redirect
  res.redirect(req.param("target"));
});

const app = require("express")();

const VALID_REDIRECT = "http://cwe.mitre.org/data/definitions/601.html";

app.get('/some/path', function(req, res) {
  // GOOD: the request parameter is validated against a known fixed string
  let target = req.param("target");
  if (VALID_REDIRECT === target)
    res.redirect(target);
});