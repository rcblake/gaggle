from flask import Blueprint, make_response, request
from flask_restful import Api, Resource
from models import PostLike
from schema import PostLikeSchema
from config import db


post_like_bp = Blueprint("post_like", __name__, url_prefix="/post_likes")
api = Api(post_like_bp)

post_likes_schema = PostLikeSchema(many=True)
post_like_schema = PostLikeSchema()


class PostLike(Resource):
    def get(self, post_like_id=None):
        if post_like_id:
            post_like = PostLike.query.get(post_like_id)
            if not post_like:
                return make_response("Post like not found", 404)
            post_like = post_like_schema.dump(post_like)
            return make_response(post_like, 200)
        else:
            post_likes = PostLike.query.all()
            post_likes = post_likes_schema.dump(post_likes)
            return make_response(post_likes, 200)

    def post(self):
        post_like_data = request.get_json()
        post_like = post_like_schema.load(post_like_data)
        db.session.add(post_like)
        db.session.commit()
        return make_response(post_like_schema.dump(post_like), 201)

    def patch(self, post_like_id):
        post_like = PostLike.query.get(post_like_id)
        if not post_like:
            return make_response("Post like not found", 404)
        post_like_data = request.get_json()
        post_like.name = post_like_data.get("name", post_like.name)
        # Update other fields as needed
        db.session.commit()
        return make_response(post_like_schema.dump(post_like), 200)

    def delete(self, post_like_id):
        post_like = PostLike.query.get(post_like_id)
        if not post_like:
            return make_response("Post like not found", 404)
        db.session.delete(post_like)
        db.session.commit()
        return make_response("Post like deleted successfully", 204)
