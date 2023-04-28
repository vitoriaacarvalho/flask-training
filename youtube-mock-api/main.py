from flask import Flask, request
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)
# this is saying we're gonna wrap our app around an api

videos = {}
class Video(Resource):
    def get(self,video_id):
        return videos[video_id]

    def put(self,video_id):
        print(request.form['likes'])
        return {}
        # for this we imported request



api.add_resource(Video, "/video/<int:video_id>")




if __name__ == "__main__":
    app.run(debug=True)
    # this is gonna start our server/application
    # debug could also be false


