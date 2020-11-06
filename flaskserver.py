from flask import Flask
import main
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

@app.route('/parkinglots')
def parkinglots():
    data = main.check_parking_lot()
    return data

if __name__ == '__main__':
    app.run()
