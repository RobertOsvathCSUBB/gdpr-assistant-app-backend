import os
from flask import Flask
from utils.auth import authenticate_google

app = Flask(__name__)

@app.route('/')
def hello_world():
    name = os.getenv('NAME', 'world')
    print(f'Hello, {name}!')
    return f'Hello, {name}!'

@app.route('/test-auth')
def test_auth():
    return authenticate_google()

if __name__ == '__main__':
    app.run(ssl_context=('cert.pem', 'key.pem'), debug=True, host='localhost', port=int(os.getenv('PORT', 5000)))