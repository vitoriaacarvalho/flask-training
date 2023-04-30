from flask import Flask, make_response, jsonify, request
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    database='cars'
)

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False  # this is to make sure the make_response items "message" and "data" come right


def execute_query(query, fetch_all=True):
    cursor = mydb.cursor()
    cursor.execute(query)
    if fetch_all:
        results = cursor.fetchall()
    else:
        results = cursor.fetchone()
    cursor.close()
    if 'select' or 'SELECT' not in query:
        mydb.commit()
    return results


@app.route("/cars", methods=['GET'])
def get_cars():

    my_cars = execute_query("select * from car")

    cars = list()  # a way of creating an empty list
    for car in my_cars:
        cars.append(
            {  # this is only to organize the response
                'id': car[0],
                'brand': car[1],
                'model': car[2],
                'year': car[3]

            }
        )
    return make_response(jsonify(message='Car List', data=cars))


@app.route('/cars', methods=['POST'])
def create_car():
    car = request.json
    sql = f'insert into car (brand, model, year) values ("{car["brand"]}","{car["model"]}", {car["year"]})'
    execute_query(sql, fetch_all=False)
    return make_response(jsonify(message='Car successfully posted', car=car))


@app.route('/cars/<int:id>', methods=['PUT'])
def update_car(id):
    car = request.json
    sql = f'update car set brand = "{car["brand"]}" , model = "{car["model"]}", \
            year = {car["year"]} where id = {id}'
    execute_query(sql, fetch_all=False)
    return make_response(jsonify(message='car updated!', car=car))


@app.route('/cars/<int:id>', methods=['DELETE'])
def delete_car(id):
    sql = f'delete from car where id = {id}'
    execute_query(sql, fetch_all=False)
    return make_response(jsonify(message='car deleted'))




app.run()