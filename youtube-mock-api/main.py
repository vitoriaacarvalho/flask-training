from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)
# this is saying we're gonna wrap our app around an api

video_post_args = reqparse.RequestParser()
video_post_args.add_argument("name", type=str, help="name of the video", required=True)
video_post_args.add_argument("views", type=int, help="views of the video", required=True)
video_post_args.add_argument("likes", type=int, help="likes on the video", required=True)

videos = {}


def abort_if_video_id_doesnt_exist(video_id):
    if video_id not in videos:
        abort(404, message="video id is not valid")


def abort_if_video_exists(video_id):
    if video_id in videos:
        abort(409, message="video already exists")


class Video(Resource):
    def get(self, video_id):
        abort_if_video_id_doesnt_exist(video_id)
        return videos[video_id]

    def post(self, video_id):
        abort_if_video_exists()
        args = video_post_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201
        # this 201 is only to let us know that it was created but its not needed
        # the parse_args gets all the arguments from the request

    def delete(self, video_id):
        abort_if_video_id_doesnt_exist()
        del videos[video_id]
        return '', 204
        # 204 stands for deleted successfully

api.add_resource(Video, "/video/<int:video_id>")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
    # this is gonna start our server/application
    # debug could also be false


