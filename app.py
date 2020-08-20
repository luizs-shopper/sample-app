import os
from datetime import datetime
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    sample_env_var = os.getenv('SAMPLE_ENV_VAR')
    return 'Hello %s!' % sample_env_var

@app.route('/health-check')
def healthcheck():
    return 'OK', 200

@app.route('/now')
def clock():
    now = datetime.now()
    return now.strftime('%d/%m/%Y %H:%M:%S')