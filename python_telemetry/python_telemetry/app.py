from flask import Flask
from elasticapm.contrib.flask import ElasticAPM

app = Flask(__name__)
app.config['ELASTIC_APM'] = {
    'SERVICE_NAME': 'python-telemetry',
    'SECRET_TOKEN': 'AAEAAWVsYXN0aWMvZmxlZXQtc2VydmVyL3Rva2VuLTE2OTMxNDgwMjE4MjY6QUE4Z3RsVVhSUFNRelp5VHdQcm91dw',
    'DEBUG': True,
    'SERVER_URL': 'http://172.31.233.100:8200',
    'ENVIRONMENT': 'my-environment',
}
apm = ElasticAPM(app, logging=True)


@app.route("/")
def hello():
    apm.capture_message('hello, world!')
    return "Hello, World!"


@app.route("/exception")
def capture_exception():
    try:
        1 / 0
    except ZeroDivisionError:
        apm.capture_exception()
        app.logger.error('Exception captured', exc_info=True)
