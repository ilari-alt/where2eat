from flask import Flask, request
from flask_cors import CORS

import main
app = Flask(__name__)
CORS(app)
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

@app.route('/10closest/<userID>')
def closest_cities(userID):
    return main.calculate_distance(userID)

@app.route('/groups/<groupID>', methods=['POST'])
def groups(groupID):
    print(groupID)
    print(request.get_data())
    if request.method == 'POST':
        return main.create_group(groupID,request.form['userID'])

if __name__ == '__main__':
    app.run()
