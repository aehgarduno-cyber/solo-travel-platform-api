from flask import Blueprint, request, jsonify, abort
from models import db, Post, PostTag, PostDestination
from models import Destination, Tag
bp=Blueprint("posts", __name__, url_prefix="/posts")

# GET /posts     || Returns all posts
@bp.route("", methods=["GET"])
def index():
    posts=Post.query.all()
    result=[]
    for p in posts:
        result.append({
            "id": p.id,
            "title": p.title,
            "body": p.body,
            "rating": p.rating,
            "is_published": p.is_published
        })
    return jsonify(result), 200

# GET /posts/    || Returns one post
@bp.route("/<int:id>", methods=["GET"])
def show(id):
    post=Post.query.get_or_404(id)
    return {
        "id": post.id,
        "title": post.title,
        "body": post.body,
        "rating": post.rating,
        "is_published": post.is_published
    }

# POST /posts    || Create a post
@bp.route("", methods=["POST"])
def create():
    data=request.get_json()
    if not data or "title" not in data:
        abort(400, description="Missing title field")
    post=Post(
        user_id=data.get("user_id", 1),  # default to your user
        title=data["title"],
        body=data.get("body", ""),
        rating=data.get("rating", None),
        is_published=data.get("is_published", False)
    )
    db.session.add(post)
    db.session.commit()
    return {"message": "Post created", "id": post.id}, 201

# PUT /posts/    || Update a post
@bp.route("/<int:id>", methods=["PUT"])
def update(id):
    post=Post.query.get_or_404(id)
    data=request.get_json()
    post.title=data.get("title", post.title)
    post.body=data.get("body", post.body)
    post.rating=data.get("rating", post.rating)
    db.session.commit()
    return {"message": "Post updated"}

# DELETE /posts/ || Delete a post
@bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    post=Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return {"message": "Post deleted"}
