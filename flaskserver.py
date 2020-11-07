from flask import Flask, request
from flask_cors import CORS
from json import loads

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


@app.route('/groups/<groupID>', methods=['POST', 'GET'])
def groups(groupID):
    if request.method == 'POST':
        data = request.get_data().decode('UTF-8')
        d = data.replace('"', "\"")
        data = loads(d)
        print("POST user", data["userID"], "to", groupID)
        return main.add_member_to_group(groupID, data["userID"])
    else:
        return main.add_member_to_group(groupID, "", "GET")


if __name__ == '__main__':
    app.run()
