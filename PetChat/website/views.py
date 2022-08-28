# Non authentication routes 

from flask import Blueprint, render_template, request
from flask_login import login_required, current_user

from .models import Leaderboard

views = Blueprint("views", __name__)


@views.route("/", methods=["GET", "POST"])
@views.route("/home", methods=["GET", "POST"])
@login_required
def home():
    # home page after logging in
    if request.method == 'POST':
        pass
    return render_template("home.html", name=current_user.username, mail_count=9)


@views.route("/newsletter", methods=["GET", "POST"])
def newsletter():
    # newsletter page
    if request.method == 'POST':
        pass
    news_content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce ullamcorper bibendum erat in condimentum. Fusce mauris ex, faucibus sit amet lobortis eu, dapibus at urna. Nam vel urna lectus. Suspendisse mattis erat quam, a ullamcorper erat lobortis quis. In eros libero, imperdiet non rhoncus placerat, porta et dolor. Fusce sit amet velit eleifend, tristique lacus a, accumsan diam. Praesent ac lacus vel turpis imperdiet scelerisque. Nullam ac enim non nulla sodales varius. Suspendisse finibus porta elit, a bibendum est tristique eget. Mauris ac augue at velit tincidunt efficitur rhoncus sit amet lectus."
    return render_template("newsletter.html", name=current_user.username, mail_count=9, newsletters=5, news_content=news_content)



@views.route("/leaderboard")
def leaderboard():
    # leaderboard page
    leaders = Leaderboard.query.order_by(Leaderboard.score.desc()).with_entities(Leaderboard.position, Leaderboard.score, Leaderboard.username).all()
    return render_template("leaderboard.html", name=current_user.username, mail_count=9, leaders=leaders)