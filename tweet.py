import requests
import tweepy
from keys import keys
from uuid import uuid1       # Use this to generate unique strings for filenames
from os import path, mkdir
import logging as log   # Logging is preferable to print() statements

random_gif_url = 'http://api.giphy.com/v1/gifs/random'

def tweet_gif(tag):

    try:
        # Authenticate to Twitter and create api object, used to send tweets
        auth = tweepy.OAuthHandler(keys['TWITTER_KEY'], keys['TWITTER_SECRET'])
        auth.set_access_token(keys['TWITTER_ACCESS_TOKEN'], keys['TWITTER_ACCESS_TOKEN_SECRET'])
        api = tweepy.API(auth)

        # Make request to URL with request parameters - API key, youth rating, tag. Requests will encode non-url characters like spaces.
        response = requests.get(random_gif_url, params = {'api_key' : keys['GIFHY_KEY'], 'rating':'y', 'tag': tag})
        response_json = response.json()
        # Extract GIF image URL from response
        image_url = response_json['data']['image_url']

        image_bytes = requests.get(image_url, stream=True)

        # Make img directory if it does not exist
        if not path.exists('img'):
            os.mkdir('img')

        filename = path.join('img', tag + str(uuid1()) + '.gif')

        # Save bytes to file specified
        with open(filename, 'wb') as gif_file:
            for chunk in image_bytes.iter_content(chunk_size=128):
                gif_file.write(chunk)

        # And post this media to Twitter, including a status (like 'KITTEN')
        api.update_with_media(filename, status=tag.upper())

        # Log message to indicate success
        log.info('Tweet sent and gif file saved at %s' % filename)

    except Exception as e:
        log.error(e)

    # TODO better error handling!
