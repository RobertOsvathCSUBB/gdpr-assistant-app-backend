import os
from flask import Flask
import flask
from utils.auth import authenticate_google, auth_callback
from log.logger import logger
from googleapiclient.discovery import build
import google.oauth2.credentials

app = Flask(__name__)

@app.route('/')
def hello_world():
    name = os.getenv('NAME', 'world')
    logger.info(f'Hello, {name}!')
    return f'Hello, {name}!'

@app.route('/test-auth')
def test_auth():
    return authenticate_google()

@app.route('/test-auth-callback')
def test_auth_callback():
    return auth_callback()

@app.route('/test-credentials')
def test_credentials():
    return flask.session['credentials']

@app.route('/test-drive')
def test_drive():
    credentials = google.oauth2.credentials.Credentials(**flask.session['credentials'])
    logger.info(f'Credentials: {credentials}')
    drive = build('drive', 'v3', credentials=credentials)
    files = drive.files().list().execute()
    return files

if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    app.run(ssl_context=('cert.pem', 'key.pem'), debug=True, host='localhost', port=int(os.getenv('PORT', 5000)))