from config import huey
import tweet

@huey.task()
def tweet_gif(tag):

    print('todo tweet %s gif' % tag)
    tweet.tweet_gif(tag)
