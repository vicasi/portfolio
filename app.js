const express = require("express");
const { log } = require("console");
const https = require("https");

const app = express();

app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static("public"));

app.listen(3000, () => {
  log("listening on 3000 ®®▄");
});

app.get("/sign-up", (req, res, err) => {
  res.sendFile(__dirname + "/signup.html");
});

app.post("/sign-up", (req, res, err) => {
  const url = "https://us21.api.mailchimp.com/3.0/lists/fffa64a025";
  let name = req.body.firstName;
  let lname = req.body.lastName;
  let email = req.body.email;
  const data = {
    members: [
      {
        email_address: email,
        status: "subscribed",
        merge_fields: {
          FNAME: name,
          LNAME: lname,
        },
      },
    ],
  };
  const jsonData = JSON.stringify(data);
  const options = {
    method: "POST",
    auth: "®®®▄:97407abb15f4699d5f3cae180eeed587-us21",
  };
  const request = https.request(url, options, (response) => {
    log(response.statusCode);
    if (response.statusCode === 200) {
      res.sendFile(__dirname + "/success.html");
    } else {
      res.redirect("/failure.html");
    }
    response.on("data", (data) => {});
  });
  request.write(jsonData);
  request.end();
});
app.get("/success.html", (req, res, err) => {
  log("success");
});

app.get("/failure.html", (req, res, err) => {
  res.sendFile(__dirname + "/failure.html");
});
app.post("/failure", (req, res, err) => {
  res.redirect("/sign-up");
});
