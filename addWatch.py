# Monte
from database import DAO
import sys
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-t", type="string", dest="term")
parser.add_option("-u", type="string", dest="user")

(options, args) = parser.parse_args()

if not options.term and not options.user:
	parser.print_help()
	sys.exit(1)


dao = DAO()

dao.addTermWatch(options.user,options.term)
