# Other routes 

from flask import Blueprint, render_template, request
from flask_login import login_required, current_user

views = Blueprint("views", __name__)


@views.route("/", methods=["GET", "POST"])
@views.route("/home", methods=["GET", "POST"])
@login_required
def home():
    if request.method == 'POST':
        pass
    return render_template("home.html", name=current_user.username, mail_count=9)