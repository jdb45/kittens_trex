## Macs and Linux

Instructions from https://redis.io/

```
wget http://download.redis.io/releases/redis-3.2.8.tar.gz
tar xzf redis-3.2.8.tar.gz
cd redis-3.2.8
make
```

To run server
```
src/redis-server
```

Leave running, open a new command line

```
src/redis-cli
monitor
```


Create and activate virtual env with, python 3

```
pip install huey
pip install redis
pip install requests
pip install tweepy
```


##PCs Use the Linux VM on the lab PCs and follow the directions above...

## All

Twitter: sign up for new account
Dev console - new app
https://apps.twitter.com/app/new

Generate access token

Create file called keys.py. Replace XXXX with your keys and secrets

```
keys = {
'GIFHY_KEY' : 'dc6zaTOxFJmzC',   # Giphy development key
'TWITTER_KEY' : 'XXXX',
'TWITTER_SECRET' : 'XXXXXX',
'TWITTER_ACCESS_TOKEN' : 'XXXX-XXXXXX',
'TWITTER_ACCESS_TOKEN_SECRET' : 'XXXXXX'
}

```

Change the menu options in main.py to gif searches of your choice.

When done, Control+C to stop the Redis server, Control+C to stop the huey_consumer tasks
