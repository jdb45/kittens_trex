from config import huey
import tweet
from tweet import *

@huey.task()
def tweet_gif(tag):
    file = tweet.tweet_gif(tag)
    return file

