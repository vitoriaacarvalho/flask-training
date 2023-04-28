from flask import Flask
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)
# this is saying we're gonna wrap our app around an api


class HelloWorld(Resource):
    # this is get overriden from Resource (and all the other methods too)
    def get(self):
        return {"data": "Hello World"}

    def post(self):
        return {"data": "Posted"}


""" the reason we return info inside a dict is because we want to make our 
response serializable and dicts are basically formatted like jsons
"""

api.add_resource(HelloWorld, "/helloworld")
# making our HelloWorld class accessible through this endpoint




if __name__ == "__main__":
    app.run(debug=True)
    # this is gonna start our server/application
    # debug could also be false


