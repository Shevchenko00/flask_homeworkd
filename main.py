from flask import Flask

app = Flask(__name__)


@app.route('/')
def home_page():
    return 'Hello, Flask!'


@app.route('/<username>')
def welcome(username):
    return f'Welcome {username}!'


if __name__ == '__main__':
    app.run(debug=True)
