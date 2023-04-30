from flask import Flask, make_response, jsonify, request
from data import Cars

app = Flask(__name__)


@app.route('/cars', methods=['GET'])
def get_cars():
    return make_response(
        jsonify(
            message='Car List',
            data=Cars
        )
    )


@app.route('/cars', methods=['POST'])
def create_car():
    car = request.json
    Cars.append(car)
    return make_response(
        jsonify(
            message='car posted',  # the name could be anything else it doesnt have to be message or car, i can choose
            car=car
        )
    )


app.run()




