import tweepy
 
 
auth1 = tweepy.auth.OAuthHandler('OSkSV1QNaj8B4U5pTpBTA','divvH9IIY19izNEjkindblILf23m4NdLHt9ONoPRx68')
auth1.set_access_token('908762354-yt3WZTtLULjlTW4FB3I5nTYwJzW6z3gdDVVMgocY','GV6iQakltxpcGELeF9a4qHoV0ZHpLaQJVxbFxEssyc')
api = tweepy.API(auth1)
# Get the User object for twitter...
user = tweepy.api.get_user('alark')

print  'User: @'+ user.screen_name
print 'Followers: '
print user.followers_count

print 'Follower Names: '

for friend in user.friends():
   print friend.screen_name
   for fakeFriends in friend.friends():
      print '\t' + fakeFriends.screen_name
      
