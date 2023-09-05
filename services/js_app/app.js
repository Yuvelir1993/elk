// Add this to the VERY top of the first file loaded in your app
const apm = require('elastic-apm-node').start({
    // Override service name from package.json
    // Allowed characters: a-z, A-Z, 0-9, -, _, and space
    serviceName: 'js-telemetry',

    // Use if APM Server requires a token
    secretToken: 'AAEAAWVsYXN0aWMvZmxlZXQtc2VydmVyL3Rva2VuLTE2OTMxNDgwMjE4MjY6QUE4Z3RsVVhSUFNRelp5VHdQcm91dw',

    // Set custom APM Server URL (default: http://127.0.0.1:8200)
    serverUrl: 'http://172.29.17.18:8200',
    environment: 'apm-telemetry'
})

const app = require('express')()

app.get('/', function (req, res) {
    res.send('Hello World from JS app!');
})

app.get('/exception', function (req, res) {
    res.status(500);
    res.send('Exception from JS app!');
    try {
        1 / 0
    } catch (error) {
        apm.captureError(error)
    }
})

app.listen(3000)