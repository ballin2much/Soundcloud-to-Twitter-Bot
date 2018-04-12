import tweepy, config, soundcloudScraper, time

auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
auth.set_access_token(config.ACCESS_KEY, config.ACCESS_SECRET)
api = tweepy.API(auth)

def findNewTrackandPost():
    message = 0
    try:
        nameandURL = soundcloudScraper.getNewestTrackNameandURL(config.MY_ID)
        message = 'New track. Listen to ' + nameandURL[0] + " " + nameandURL[1]
        api.update_status(message)
        print(message + ' was tweeted.')
    except TypeError:
        print('No new track.')
    except:
        print('Unsure about error.')
    
while True:
    findNewTrackandPost()
    time.sleep(600)