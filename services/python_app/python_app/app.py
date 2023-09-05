import requests
from flask import Flask, Response
from elasticapm.contrib.flask import ElasticAPM

app = Flask(__name__)
app.config['ELASTIC_APM'] = {
    'SERVICE_NAME': 'python-telemetry',
    'SECRET_TOKEN': 'AAEAAWVsYXN0aWMvZmxlZXQtc2VydmVyL3Rva2VuLTE2OTMxNDgwMjE4MjY6QUE4Z3RsVVhSUFNRelp5VHdQcm91dw',
    'DEBUG': True,
    'SERVER_URL': 'http://172.29.17.18:8200',
    'ENVIRONMENT': 'apm-telemetry',
}
apm = ElasticAPM(app, logging=True)


@app.route("/", methods=['GET'])
def hello():
    apm.capture_message('hello, world from Python app!')
    return "Hello, World!"


@app.route("/exception", methods=['GET'])
def capture_exception():
    try:
        1 / 0
    except ZeroDivisionError:
        apm.capture_exception()
        app.logger.error('Exception captured', exc_info=True)


@app.route("/callJs", methods=['GET'])
def call_js():
    apm.capture_message('Calling js application.')
    r = requests.get("http://localhost:3000")
    return Response(
        r.text,
        status=r.status_code,
        content_type=r.headers['content-type'],
    )


@app.route("/callJsException", methods=['GET'])
def call_js_exception():
    apm.capture_message('Calling js application which will throw exception.')
    r = requests.get("http://localhost:3000/exception")
    return Response(
        r.text,
        status=r.status_code,
        content_type=r.headers['content-type'],
    )
