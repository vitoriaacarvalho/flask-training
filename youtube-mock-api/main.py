from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)
# this is saying we're gonna wrap our app around an api

video_post_args = reqparse.RequestParser()
video_post_args.add_argument("name", type=str, help="name of the video", required=True)
video_post_args.add_argument("views", type=int, help="views of the video", required=True)
video_post_args.add_argument("likes", type=int, help="likes on the video", required=True)

"""
line 8 means we're gonna make a new request parser object and it will parse through the request thats being sent
and make sure that it fits the guideline we created and has the right information in it.

lines 9-11 are saying "this is something that needs to be sent with the request"
"name" is essentially the name of the key that needs to be sent of TYPE string and HELP is what we should display
to the sender if they dont send us this name argument (basically an error message)
"""

videos = {}


class Video(Resource):
    def get(self, video_id):
        return videos[video_id]

    def post(self, video_id):
        args = video_post_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201
        # this 201 is only to let us know that it was created but its not needed
        # the parse_args gets all the arguments from the request


api.add_resource(Video, "/video/<int:video_id>")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
    # this is gonna start our server/application
    # debug could also be false


