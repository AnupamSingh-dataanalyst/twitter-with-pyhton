import tweepy 

#Add your credentials here
twitter_keys = {
        'consumer_key':        'xxxxxxxxxxxxxxxxxxxxxxxx',
        'consumer_secret':     'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
        'access_token_key':    'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
        'access_token_secret': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
}
    
#Setup access to API
auth = tweepy.OAuthHandler(twitter_keys['consumer_key'], twitter_keys['consumer_secret'])
auth.set_access_token(twitter_keys['access_token_key'], twitter_keys['access_token_secret'])
api =tweepy.API(auth,wait_on_rate_limit=True)

#Search stuff
def main():
search_results = tweepy.Cursor(api.search, q = "#vaccination is:verified").items(5)
for result in search_results:
    print(result.text)
    print(result.user.screen_name)
    print(result.user.location)
 
if __name__ == "__main__":
    main()