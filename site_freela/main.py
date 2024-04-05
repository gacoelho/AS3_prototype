from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/sobre_nos')
def sn():
    return render_template('sn.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/academy')
def academy():
    return render_template('academy.html')

@app.route('/sucess')
def sucess():
    return render_template('sucess.html')

if __name__ == '__main__':
    app.run(debug=True)
