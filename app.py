#!/usr/bin/env python3

from flask import Flask, render_template
from flask_mongoengine import MongoEngine

# this will change once we start using app factories
# http://docs.mongoengine.org/projects/flask-mongoengine/en/latest/
app = Flask(__name__)
## include db name in URI; it overwrites all others
app.config['MONGODB_HOST'] = 'mongodb://localhost:27017/sivji-sandbox'
db = MongoEngine()
db.init_app(app)

class Post(db.Document):
    ''' Class for defining structure of reddit-top-posts collection
    '''
    url = db.URLField(required=True)
    date = db.DateTimeField(required=True)
    commentsUrl = db.URLField(required=True)
    sub = db.StringField(max_length=20, required=True) # subredit can be 20 chars
    title = db.StringField(max_length=300, required=True) # title can be 300 chars
    score = db.IntField(required=True)

    meta = {
        'collection': 'top_reddit_posts', # collection name
        'ordering': ['-score'], # default ordering
        'auto_create_index': False, # MongoEngine will not create index
        }

@app.route("/")
def get_top_posts():
    ## get the last date the webscraper was run
    for post in Post.objects().fields(date=1).order_by('-date').limit(1):
        day_to_pull = post.date.date()

    # return render_template('template.html', Post=Post, day_to_pull=day_to_pull)
    return render_template(
        'template.html',
        Post=Post,
        day_to_pull=day_to_pull)

if __name__ == "__main__":
    app.run()
