'''
Requirements

Username must contain a lowercase letter
Username must contain an uppercase letter
Username must contain end in a number
'''

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/report')
def report():
    username = request.args.get('username')
    cond1 = cond2 = cond3 = False

    for letter in username:
        if(letter.islower()):
            cond1 = True
        elif(letter.isupper()):
            cond2 = True

    if(username[-1].isnumeric()):
        cond3 = True


    return render_template('report.html', cond1=cond1, cond2=cond2, cond3=cond3)

if __name__ == '__main__':
    app.run(debug=True)