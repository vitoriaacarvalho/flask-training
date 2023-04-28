from flask import Flask
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)
# this is saying we're gonna wrap our app around an api

names = {"tim": {"age": 19 , "gender": "male"},
         "bill": {"age": 23, "gender": "male"}}


class HelloWorld(Resource):
    # this is get overriden from Resource (and all the other methods too)
    def get(self,name):
        return names[name]



api.add_resource(HelloWorld, "/helloworld/<string:name>")





if __name__ == "__main__":
    app.run(debug=True)
    # this is gonna start our server/application
    # debug could also be false


