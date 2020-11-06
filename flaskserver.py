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


@app.route('/city/<cityname>')
def city(cityname):
    data = main.check_city(cityname)
    return data

@app.route('/10closest')
def closest_cities():
    return main.calculate_distance(23.7526973,-99.1633594)


if __name__ == '__main__':
    app.run()
