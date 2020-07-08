import flask
import time
import json
import os

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    epoch_time = int(time.time())
    return json.dumps(
        {
            'message': 'Automate all the things!',
            'timestamp': epoch_time
        })

#make port configurable
server_port = os.environ.get('WEBSERVER_PORT') or 5000
app.run(port=server_port)