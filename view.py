from flask import render_template
from model import Post

### HELPER FUNCTIONS
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
    params = {field: 1} # pass in as keyword arguments
    return list(Post.objects().fields(**params).distinct(field))

### VIEWS
def index():
    day_to_pull = get_last_rundate()

    return render_template(
        'index.html',
        Post=Post,
        day_to_pull=day_to_pull
        )

def all_dates():
    dates = posts_get_distinct_items('date_str')

    return render_template(
        'all-dates.html',
        dates=reversed(dates) # latest date on top
        )

def by_date(day_to_pull=None):
    return render_template(
        'index.html',
        Post=Post,
        day_to_pull=day_to_pull
        )

def all_subreddits():
    subs = posts_get_distinct_items('sub')

    return render_template(
        'all-subreddits.html',
        subs=sorted(subs, key=str.lower) # sort list of subreddits
        )

def by_subreddit(sub_to_pull=None):
    return render_template(
        'by-subreddit.html',
        Post=Post,
        sub=sub_to_pull
        )
