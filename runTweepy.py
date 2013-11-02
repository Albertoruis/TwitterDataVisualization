# Alberto
import tweepy
import re
import sys
import datetime
from datetime import date
from optparse import OptionParser
from database import DAO


#User & term to look at.
parser = OptionParser()
parser.add_option("-u", type="string", dest="user")
parser.add_option("-t", type="string", dest="term")
(options, args) = parser.parse_args()

if not options.user or not options.term:
	print "Usage: -u 'alark' -t 'graphics' -d 'MM/DD/YYYY'\n"
	sys.exit(1)



#Database initialization
dao = DAO()
hits = 0
user = options.user
term = options.term
dateToHits = {}

#Gets Tweets using Auth. Call & searchs for a keyword
def getTweetsAuth(name, idea):
    global hits
    global dateToHits
    for tweet in tweepy.Cursor(auth.user_timeline, screen_name = name,include_rts=0, count =300).items(300):
        dayCreated = tweet.created_at
        if not dayCreated.date() in dateToHits:
            dateToHits[dayCreated.date()] = 0
        print tweet.text
        # Splits the up the line into words by using [_.,;: *\'\"@#&!?-]+ as delimters
        for words in re.split('[_.,;: *\'\"@#&!?-]+',tweet.text, maxsplit=0,flags=0):
            for word in words.split():
                lowerWord = word.lower()
                if term.lower()==lowerWord:
                    dateToHits[dayCreated.date()] += 1
        print dateToHits[dayCreated.date()]

#Gets Tweets using Public access searchs for a keyword
def getTweets(name, idea):
    global hits
    global dateToHits
    for tweet in tweepy.Cursor(tweepy.api.user_timeline, screen_name = name,include_rts=0, count =300).items(300):
        dayCreated = tweet.created_at
        if not dayCreated.date() in dateToHits:
            dateToHits[dayCreated.date()] = 0
        # Splits the up the line into words by using [_.,;: *\'\"@#&!?-]+ as delimters
        for words in re.split('[_.,;: *\'\"@#&!?-]+',tweet.text, maxsplit=0,flags=0):
            for word in words.split():
                lowerWord = word.lower()
                if term.lower()==lowerWord:
                    dateToHits[dayCreated.date()] += 1

#Authorization for 350 requests
auth1 = tweepy.auth.OAuthHandler('OSkSV1QNaj8B4U5pTpBTA','divvH9IIY19izNEjkindblILf23m4NdLHt9ONoPRx68')
auth1.set_access_token('908762354-yt3WZTtLULjlTW4FB3I5nTYwJzW6z3gdDVVMgocY','GV6iQakltxpcGELeF9a4qHoV0ZHpLaQJVxbFxEssyc')
auth = tweepy.API(auth1)


# if auth rate is less than 10 , else use public, else quit
def runUserWithTerm(user,term):

    print "tweet"
    global dateToHits
    if auth.rate_limit_status()['remaining_hits'] >10:
        getTweetsAuth(user,term)
    elif tweepy.api.rate_limit_status()['remaining_hits'] >50:
        getTweets(user,term)
    else:
        for key in dateToHits:
            dao.insertHits(user, term, dateToHits[key], key)
        dao.closeDatabase()
        sys.exit(1)

# Starts the Tweet searching process
runUserWithTerm(user,term)

#Get's first 100 people that the user is following & search their tweets
friends = auth.get_user(user).friends()[:100]
for friend in friends:
    if not friend.protected:
        runUserWithTerm(friend.screen_name, term)

#Inserts Items in Database
for key in dateToHits:
    dao.insertHits(user, term, dateToHits[key], key)
dao.closeDatabase()






        
    


		
