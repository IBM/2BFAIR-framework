// Copyright (C) 2025 IBM Corp.
// SPDX-License-Identifier: Apache-2.0

const express = require("express");
const path = require("path");
const cors = require("cors");

const angularFilesDirectory = path.join(
  __dirname,
  "..",
  "dist",
  "frontend",
  "browser"
);

// create a new express server
const app = express();

app.use(cors());

app.get("/get-backend", (req, res) => {
  res.send(process.env.BACKEND_URL ?? "http://localhost:8000");
});

// serve the files out of root dir as our main files
// (server.js should be copied to the dist folder BEFORE pushing to Bluemix)
app.use(express.static(angularFilesDirectory));

// For all GET requests, send back index.html
// so that PathLocationStrategy can be used
app.get("/*", (req, res) => {
  const filepath = path.join(angularFilesDirectory, "index.html");
  res.sendFile(filepath);
});

const SERVER = "0.0.0.0";
const PORT = process.env.PORT || 42000;

// start server on the specified port and binding host
app.listen(PORT, SERVER, () => {
  // print a message when the server starts listening
  console.log(`server starting on ${SERVER}:${PORT}`);
});
