import tweepy

auth1 = tweepy.auth.OAuthHandler('OSkSV1QNaj8B4U5pTpBTA','divvH9IIY19izNEjkindblILf23m4NdLHt9ONoPRx68')
auth1.set_access_token('908762354-yt3WZTtLULjlTW4FB3I5nTYwJzW6z3gdDVVMgocY','GV6iQakltxpcGELeF9a4qHoV0ZHpLaQJVxbFxEssyc')
api = tweepy.API(auth1)




print "Auth Calls remaining:"
print api.rate_limit_status()['remaining_hits']

print "\nPublic Calls remaining:"
print tweepy.api.rate_limit_status()['remaining_hits']

    

