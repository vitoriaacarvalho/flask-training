from flask import Flask
from data import Cars

app = Flask(__name__)


@app.route('/cars', methods=['GET'])
def get_cars():
    return Cars


app.run()




