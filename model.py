from flask_mongoengine import MongoEngine

db = MongoEngine()


class Post(db.Document):
    """Class for defining structure of reddit-top-posts collection
    """
    url = db.URLField(required=True)
    date = db.DateTimeField(required=True)
    date_str = db.StringField(max_length=10, required=True)
    commentsUrl = db.URLField(required=True)
    sub = db.StringField(max_length=20, required=True) # subreddit can be 20 chars
    title = db.StringField(max_length=300, required=True) # title can be 300 chars
    score = db.IntField(required=True)

    meta = {
        'collection': 'top_reddit_posts', # collection name
        'ordering': ['-score'], # default ordering
        'auto_create_index': False, # MongoEngine will not create index
        }
