from flask import Flask, request, send_from_directory, send_file, render_template
import os
from urllib.parse import unquote, unquote_plus
app = Flask(__name__)

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('src/js', path)

@app.route('/styles/<path:path>')
def send_styles(path):
    return send_from_directory('src/styles', path)

@app.route('/')
def send_home():
    return send_from_directory('src/html', 'index.html')

@app.route('/twitterStuff')
def print_ver():
    return f"paste this into your terminal: {request.args.get('oauth_verifier')}"

@app.route('/reademail')
def read_email():
    emailaddress = request.args.get("address")
    subjectline = request.args.get("subject")
    with open('/home/ellie/elliesite/emaillog.txt', 'a') as f:
        f.write(f'{subject} opened by {emailaddress}')
    return send_from_directory('/src', '1x1.png')

@app.route('/EG')
def send_EG_file():
    return send_from_directory('EG', request.args.get('file'))

@app.route('/AR')
def send_AR_file():
    return send_from_directory('AR', request.args.get('file'))

if __name__ == "__main__":
    app.run(host='0.0.0.0')
