from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<p>EBA</p>'

@app.route('/information/')
def info():
    return '<div>nice info</div>'

if __name__ == "__main__":
    app.run()