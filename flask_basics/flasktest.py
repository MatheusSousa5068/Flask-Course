from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<p>EBA</p>'

@app.route('/information/')
def info():
    return '<div>nice info</div>'

@app.route('/user/<name>')
def user(name: str):
    return f'<p>User: {name}</p>'


if __name__ == "__main__":
    app.run()