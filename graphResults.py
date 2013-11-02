# Clayton
from database import DAO
import matplotlib.pyplot as plt
from datetime import datetime
from optparse import OptionParser
import sys


# Class to define accessor functions
class GraphResults:

    watches = {}
    results = {}

    # Get a list of watched (user, term) combinations
    def setWatches(self, dao):
        for user, term in dao.getUsersAndTerms():
            self.watches.setdefault(str(user), []).append(str(term))

    # extract the users from the dictionary watches
    def getUsers(self):
        return self.watches.keys()

    # extract the terms from the dictionary watches
    def getTerms(self, usr):
        return self.watches.get(usr)

    # put the results from a search into a dictionary
    def setResults(self, dao, user, term):
        r = dao.getResults(user, term)
        self.results = dict(r)

    # convert a date string to a datetime obj
    def getDates(self):
        dateArray = self.results.keys()
        returnDates = []
        for date in dateArray:
            returnDates.append(datetime.strptime(date, '%Y-%m-%d'))
        return returnDates

    # get count from results
    def getCount(self):
        return self.results.values()

    # create and show graph
    def makeGraph(self, user, term, dates, count):
        plt.plot_date(dates,count,'m.')
        plt.title("%s and Friends\n are tweeting about: %s" %(user, term))
        plt.ylabel('Number of Hits')
        plt.xlabel('Date')
        plt.show()


# main method so to speak
class GetGraph():
    def __init__(self, parrent=None):
        dao  = DAO()
        gr = GraphResults()
        gr.setWatches(dao)

        parser = OptionParser()
        parser.add_option("-u", type="string", dest="user")
        parser.add_option("-t", type="string", dest="term")

        (options, args) = parser.parse_args()
        # make sure correct args passed
        if not options.user or not options.term:
            print "Usage: -u 'name of user' -t 'term to graph'\n"
            sys.exit(1)

        gr.setResults(dao, options.user, options.term)

        print "Counts: \n", gr.getCount()
        print "Dates: \n", gr.getDates()

        gr.makeGraph(options.user, options.term, gr.getDates(), gr.getCount())

graph = GetGraph(sys.argv)
#dao = DAO()
#print dao.getAllHits()
#print dao.getUsersAndTerms()
