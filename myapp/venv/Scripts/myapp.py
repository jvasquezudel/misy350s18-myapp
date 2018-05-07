from flask import Flask
app = Flask(__name__)
import random


@app.route('/')
def index():
    return "Hello Jose Vasquez-Fonseca"

@app.route('/hello')
def user():
    greeting_list = ['Ciao', 'Hei', 'Salut', 'Hola', 'Nihao']
    return random.choice(greeting_list)


if __name__ == '__main__':
    app.run()
