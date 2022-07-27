const express = require('express');
const bodyParser = require('body-parser');
const request = require('request');
const https = require('https');

const app = express();

app.use(bodyParser.urlencoded({ extended: true }));

app.use(express.static('public'));

app.get('/', function (req, res, err) {
    res.sendFile(__dirname + '/signup.html');
});

app.post('/', function (req, res, err) {
    const firstName = req.body.firstName;
    const lastName = req.body.lastName;
    const email = req.body.email;
    let data = {
        members: [
            {
                email_address: email,
                status: 'subscribed',
                merge_fields: {
                    FNAME: firstName,
                    LNAME: lastName,
                },
            },
        ],
    };
    const jData = JSON.stringify(data);
    const url = 'https://us11.api.mailchimp.com/3.0/lists/8c327c8189';
    const options = {
        method: 'post',
        auth: 'vio:2055d004af4bdc7d5181844a54cd4380-us11',
    };

    const request = https.request(url, options, function (response) {
        if (response.statusCode == 200) {
            res.sendFile(__dirname + '/success.html');
        } else {
            res.sendFile(__dirname + '/failure.html');
        }
    });
    request.write(jData);
    request.end();
});

app.post('/failure', function (req, res, err) {
    res.sendFile(__dirname + '/signup.html');
});

app.listen(process.env.PORT || 3000, function (req, res, err) {
    console.log('running');
});
