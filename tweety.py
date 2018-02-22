import tweepy

consumer_token="UFqzQro5WmCDixHKooArJKNtn"
consumer_secret="8ePAtzTk2hJNRiXQYfAS00rZYeQhw2VlwgqceLIWGcm5jkg5lM"
access_token="2485607774-yvbUSLkTRQXEacGqyXL0O4AFMl5ir7IPJKfcltn"
access_token_secret="d9YJ731AN6anZqus8NarRHgtGJqzWPTaUIKk1ZgZqx7Ei"

auth = tweepy.OAuthHandler(consumer_token,consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

