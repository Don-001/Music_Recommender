from flask import Blueprint, render_template, request
from flask_login import login_required, current_user



views = Blueprint('views', __name__)


@views.route('/', methods= ['POST', 'GET'])
@login_required
def search():
   return render_template("search.html", user=current_user)
