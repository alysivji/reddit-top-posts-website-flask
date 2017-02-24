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


@app.route("/")
def index():
    ## get the last date the webscraper was run
    for post in Post.objects().fields(date=1).order_by('-date').limit(1):
        day_to_pull = post.date.date()

    print (type(day_to_pull))

    return render_template(
        'index.html',
        Post=Post,
        day_to_pull=day_to_pull)

if __name__ == "__main__":
    app.run()
