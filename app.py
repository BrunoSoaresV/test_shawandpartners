import requests
from flask import Flask, request

app = Flask(__name__)

@app.route('/api/users', methods=['GET'])
def users():
    since = request.args.get('since')
    response = requests.get(f'https://api.github.com/users?since={since}')
    return response.text, response.status_code

@app.route('/api/users/<username>/details', methods=['GET'])
def user_details(username):
    response = requests.get(f'https://api.github.com/users/{username}')
    return response.text, response.status_code

@app.route('/api/users/<username>/repos', methods=['GET'])
def user_repos(username):
    response = requests.get(f'https://api.github.com/users/{username}/repos')
    return response.text, response.status_code

if __name__ == '__main__':
    app.run()
