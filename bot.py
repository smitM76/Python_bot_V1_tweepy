
import tweepy

consumer_key = 'aq2PB5jMDKR7qcRbdzYP9bh8q'
consumer_secret = 'CkkNPjVRAg4CGXeNNsIad2NrgsFOb3fmBu0okM5Vk59AOZ2bDr'
access_token = '1069468297853251590-gqq92bsEXaGOF6BYl5XyIEJ9I6OvfK'
access_secret = '1IIy5gBFp3Jn1aKluHpEvzhb527YVF0URByqQxjTqfnkS'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

mentions = api.mentions_timeline()

for mention in mentions:
    #print(str(mention.id + ' \t ' + mention.text))
    #print('{} {}'.format(mention.id, mention.text))
    if 'helloworld' in mention.text.lower():

        print('{} {}'.format(mention.id, mention.text))
        try:
            api.update_status('@' + mention.user.screen_name +
                              '#helloworld back to you', mention.id)
            print('replied to {}'.format(mention.user.screen_name))

        except tweepy.TweepError:
            pass

        #print('found helloworld')
    else:
        break
