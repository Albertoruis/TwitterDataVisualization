# Clayton

from database import DAO

import matplotlib.pyplot as plt
from datetime import datetime
from optparse import OptionParser
import sys

dao = DAO()

u1 = 'alark'
u2 = 'bjo3rn'
t1 = 'graphics'
t2 = 'code'

print dao.getUsersAndTerms()
print dao.getAllHits()
print dao.getAllHits()

print dao.getResults(u1, t1)
print dao.getResults(u2, t1)
print dao.getResults(u1, t2)
