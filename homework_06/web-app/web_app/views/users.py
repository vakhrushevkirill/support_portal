from flask import Blueprint, request, jsonify, render_template, url_for, redirect
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import NotFound, BadRequest, InternalServerError

from web_app.models import db
from web_app.models import User

users_app = Blueprint("users_app", __name__, url_prefix="/users")


@users_app.route("/", endpoint="list")
def list_users():
    users = User.query.all()
    return render_template("users/index.html", users=users)


@users_app.route("/<int:user_id>/", endpoint="details")
def get_user(user_id):
    user = User.query.filter_by(id=user_id).one_or_none()
    if user is None:
        raise NotFound(f"User #{user_id} doesn't exist.")
    return render_template(
        "users/details.html",
        user=user,
    )


@users_app.route("/add/", methods=["GET", "POST"], endpoint="add")
def add_user():
    if request.method == "GET":
        return render_template("users/add.html")

    user_name = request.form.get("user-name")
    if not user_name:
        raise BadRequest("Field user-name is required!")

    user = User(name=user_name)
    db.session.add(user)

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise InternalServerError(f"Could not save user with name {user_name!r}")

    url = url_for("users_app.details", user_id=user.id)
    return redirect(url)
