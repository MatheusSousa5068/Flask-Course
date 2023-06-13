from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    var = 'Pablo'
    letters = list(var)
    return render_template('basic.html', name=var, letters=letters)



if __name__ == '__main__':
    app.run(debug=True)