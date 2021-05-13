import tweepy


# Authenticate with Twitter API using OAuth
def authenticate():
    consumerKey = ''
    consumerSecret = ''

    accessToken = ''
    accessTokenSecret = ''

    auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
    auth.set_access_token(accessToken, accessTokenSecret)

    api = tweepy.API(auth)
    print(f'Account: {api.me().name}')

    return api


# Upload media to Twitter
def upload(imagePath, api):
    api.update_with_media(imagePath)
