# Monte
from database import DAO
import sys
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-t", type="string", dest="term")
parser.add_option("-u", type="string", dest="user")
parser.add_option("-n", type="string", dest="hits")

(options, args) = parser.parse_args()

if not options.term or not options.user or not options.hits:
	parser.print_help()
	sys.exit(1)

dao = DAO()

dao.insertHits(options.user, options.term, options.hits)

