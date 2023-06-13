# lucas -> lucasy
# yasminy -> yasminiful

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<p>EBA</p>'

@app.route('/<name>')
def user(name: str):
    return f'<p>{name_handler(name)}</p>'

# Convert name
def name_handler(name):
    if name[-1] != 'y':
        name += 'y'
        name = name[:-1] + 'iful'

    return name


if __name__ == "__main__":
    app.run(debug=True)