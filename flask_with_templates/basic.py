from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    var = 'Pablo'
    letters = list(var)

    students = ['Matheus', 'Pablo', 'Marcela']

    is_logged = False
    return render_template('basic.html', letters=letters, students=students, is_logged = is_logged)



if __name__ == '__main__':
    app.run(debug=True)