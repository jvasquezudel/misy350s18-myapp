from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form')
def form_basics():
    return render_template('form.html')

@app.route('/form-demo')
def form_demo():
    return "<h1>You have submitted the form</h1>"

@app.route('/users/<string:username>')
def username(username):
    return render_template('users.html', username = username)


if __name__ == '__main__':
    app.run()
