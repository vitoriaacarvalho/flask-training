from flask import Flask, make_response, jsonify
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    database='cars'
)

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False  # this is to make sure the make_response items "message" and "data" come right


@app.route("/cars", methods=['GET'])
def get_cars():
    cursor = mydb.cursor()
    cursor.execute("select * from car")
    my_cars = cursor.fetchall()

    cars = list() # a way of creating an empty list
    for car in my_cars:
        cars.append(
            {
                'id': car[0],
                'brand': car[1],
                'model': car[2],
                'year': car[3]

            }
        )
    return make_response(
        jsonify(
            message='Car List',
            data=cars
        )
    )


app.run()