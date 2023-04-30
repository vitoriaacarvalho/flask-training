from flask import Flask, make_response, jsonify, request
from data import Cars

app = Flask(__name__)


@app.route('/cars', methods=['GET'])
def get_cars():
    return make_response(
        jsonify(Cars)
    )
# make_response is used to create a personalized response (when we dont use it flask returns a tuple
# jsonify is used to serialize objects and return them as http responses


@app.route('/cars', methods=['POST'])
def create_car():
    car = request.json
    Cars.append(car)
    return car


app.run()




