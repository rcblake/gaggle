from flask import Blueprint, make_response, request
from flask_restful import Api, Resource
from models import Comment
from schema import CommentSchema
from config import db


comment_bp = Blueprint("comment", __name__, url_prefix="/api/v1/comments")
api = Api(comment_bp)

comments_schema = CommentSchema(many=True)
comment_schema = CommentSchema()


class CommentBP(Resource):
    def get(self, comment_id=None):
        if comment_id:
            comment = Comment.query.get(comment_id)
            if not comment:
                return make_response("Comment not found", 404)
            comment = comment_schema.dump(comment)
            return make_response(comment, 200)
        else:
            comments = Comment.query.all()
            comments = comments_schema.dump(comments)
            return make_response(comments, 200)

    def post(self):
        comment_data = request.get_json()
        comment = comment_schema.load(comment_data)
        db.session.add(comment)
        db.session.commit()
        return make_response(comment_schema.dump(comment), 201)

    def patch(self, comment_id):
        comment = Comment.query.get(comment_id)
        if not comment:
            return make_response("Comment not found", 404)
        comment_data = request.get_json()
        comment.name = comment_data.get("name", comment.name)
        # Update other fields as needed
        db.session.commit()
        return make_response(comment_schema.dump(comment), 200)

    def delete(self, comment_id):
        comment = Comment.query.get(comment_id)
        if not comment:
            return make_response("Comment not found", 404)
        db.session.delete(comment)
        db.session.commit()
        return make_response("Comment deleted successfully", 204)
