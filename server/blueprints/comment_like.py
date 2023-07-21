from flask import Blueprint, make_response, request
from flask_restful import Api, Resource
from models import CommentLike
from schema import CommentLikeSchema
from config import db


comment_like_bp = Blueprint(
    "comment_like", __name__, url_prefix="/api/v1/comment_likes"
)
api = Api(comment_like_bp)

comment_likes_schema = CommentLikeSchema(many=True)
comment_like_schema = CommentLikeSchema()


class CommentLikeBP(Resource):
    def get(self, comment_like_id=None):
        if comment_like_id:
            comment_like = CommentLike.query.get(comment_like_id)
            if not comment_like:
                return make_response("Comment like not found", 404)
            comment_like = comment_like_schema.dump(comment_like)
            return make_response(comment_like, 200)
        else:
            comment_likes = CommentLike.query.all()
            comment_likes = comment_likes_schema.dump(comment_likes)
            return make_response(comment_likes, 200)

    def post(self):
        comment_like_data = request.get_json()
        comment_like = comment_like_schema.load(comment_like_data)
        db.session.add(comment_like)
        db.session.commit()
        return make_response(comment_like_schema.dump(comment_like), 201)

    def patch(self, comment_like_id):
        comment_like = CommentLike.query.get(comment_like_id)
        if not comment_like:
            return make_response("Comment like not found", 404)
        comment_like_data = request.get_json()
        comment_like.name = comment_like_data.get("name", comment_like.name)
        # Update other fields as needed
        db.session.commit()
        return make_response(comment_like_schema.dump(comment_like), 200)

    def delete(self, comment_like_id):
        comment_like = CommentLike.query.get(comment_like_id)
        if not comment_like:
            return make_response("Comment like not found", 404)
        db.session.delete(comment_like)
        db.session.commit()
        return make_response("Comment like deleted successfully", 204)
