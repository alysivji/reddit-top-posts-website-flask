#!/usr/bin/env python3

from flask import Flask, render_template
from flask_mongoengine import MongoEngine
from models import db, Post

# this will change once we start using app factories
# http://docs.mongoengine.org/projects/flask-mongoengine/en/latest/
app = Flask(__name__)

## include db name in URI; it overwrites all others
app.config['MONGODB_HOST'] = 'mongodb://localhost:27017/sivji-sandbox'
app.debug = True

# initalize app with database
db.init_app(app)

def get_last_rundate():
    """Gets the last run date from the database

    Arg:
        None

    Returns:
        date_str field (format: 'YYYY-MM-DD')
    """
    # run a query to grab the last post
    for post in Post.objects().fields(date_str=1).order_by('-date_str').limit(1):
        return post.date_str

def posts_get_distinct_items(field):
    """Get list of distinct items contained in the Post collection

    Arg:
        field: field name we want distinct items for

    Returns:
        list of distinct items
    """
    # pass in as keyword arguments
    params = {field: 1}
    return list(Post.objects().fields(**params).distinct(field))


@app.route("/")
def index():
    day_to_pull = get_last_rundate()

    return render_template(
        'index.html',
        Post=Post,
        day_to_pull=day_to_pull
        )

@app.route("/date")
def all_dates():
    dates = posts_get_distinct_items('date_str')

    return render_template(
        'all-dates.html',
        dates=reversed(dates) # latest date on top
        )

@app.route("/date/<day_to_pull>")
def by_date(day_to_pull=None):
    return render_template(
        'index.html',
        Post=Post,
        day_to_pull=day_to_pull
        )

@app.route("/sub")
def all_subs():
    subs = posts_get_distinct_items('sub')

    return render_template(
        'all-subreddits.html',
        subs=sorted(subs, key=str.lower) # sort list of subreddits
        )

@app.route("/sub/<sub_to_pull>")
def by_subreddit(sub_to_pull=None):
    return render_template(
        'by-subreddit.html',
        Post=Post,
        sub=sub_to_pull
        )


if __name__ == "__main__":
    app.run()
