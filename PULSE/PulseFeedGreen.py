 
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import json


ckey = 'LstGjWjU7uZ4CfA664L4qbc0O'
csecret = '6qPhbKOEXhJckDjw7AktGHzLxAxNLYfUa77A4H6Xe9dZBlNwHP'
atoken = '4011918614-CkjsxvdJQaUmew07VvPo03qRVmRvt4S1t41UIJa'
asecret = 'lTHEDr2XmfaR2Wy7NEVIzVEjBZyyIont9h1cdf8W0Whnm'

class listener (StreamListener):

    def on_data(self, data):
        try:
            all_data = json.loads(data)

            tweet = all_data["text"]
            username = all_data["user"]["name"]
            created = all_data["created_at"]

        
            print 'User: ', ((username))
            print 'Date: ', ((created))
            print 'Tweet: ', ((tweet))
            print '\n\n'

            saveFile = open('DATABASE_GREEN.xml','a')
            saveFile.write(created+':::'+username+':::'+tweet+':::')
            saveFile.write('\n')
            saveFile.close()
            
            return True
            
        except Exception as e:
            print 'failed on data,',str(e)
            time.sleep(5)



    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=['happy', 'success', 'potential', 'blessed', 'joy', 'laughing', 'sweet', 'good', 'pleased', 'and'])



