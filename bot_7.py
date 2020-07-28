# import the package tweepy
import tweepy

def main():

    # replace these keys by your own keys
    # from the twitter developer account
    twitter_auth_keys = {
        "consumer_key" : "FOiLSyJd2oebzN0Dp6MxQqt8A",
        "consumer_secret" : "Vimxt4eN5djhd6c5j47S2ZJZsErNliXnYZ0QzFMd55bHM95JRz",
        "access_token" : "1217847361009045507-FUievTy4u3byJT3GZYjHoiCR5wWnPa",
        "access_token_secret" : "0oYdgA5T8uI4VfJZDplStUKXdg7x4GJZOkpn7UGqa9fpQ"
    }

    auth = tweepy.OAuthHandler(
        twitter_auth_keys['consumer_key'],
        twitter_auth_keys['consumer_secret']
    )

    auth.set_access_token(
        twitter_auth_keys['access_token'],
        twitter_auth_keys['access_token_secret']
    )

    api = tweepy.API(auth)

    # this is to search for trends
    trends_results = api.trends_place(1)
    for trend in trends_results[0]['trends']:
        print(trend['name'])

main()