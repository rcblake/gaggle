from flask import Blueprint, make_response, request
from flask_restful import Api, Resource
from models import Post
from schema import PostSchema
from config import db


post_bp = Blueprint("post", __name__, url_prefix="/posts")
api = Api(post_bp)

posts_schema = PostSchema(many=True)
post_schema = PostSchema()


class PostBP(Resource):
    def get(self, post_id=None):
        if post_id:
            post = Post.query.get(post_id)
            if not post:
                return make_response("Post not found", 404)
            post = post_schema.dump(post)
            return make_response(post, 200)
        else:
            posts = Post.query.all()
            posts = posts_schema.dump(posts)
            return make_response(posts, 200)

    def post(self):
        post_data = request.get_json()
        post = post_schema.load(post_data, session=db.session)
        db.session.add(post)
        db.session.commit()
        return make_response(post_schema.dump(post), 201)

    def patch(self, post_id):
        post = Post.query.get(post_id)
        if not post:
            return make_response("Post not found", 404)
        post_data = request.get_json()
        post.name = post_data.get("name", post.name)
        # Update other fields as needed
        db.session.commit()
        return make_response(post_schema.dump(post), 200)

    def delete(self, post_id):
        post = Post.query.get(post_id)
        if not post:
            return make_response("Post not found", 404)
        db.session.delete(post)
        db.session.commit()
        return make_response("Post deleted successfully", 204)
