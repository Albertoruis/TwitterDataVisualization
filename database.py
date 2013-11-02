#!/usr/bin/python
# Monte

import sqlite3 as lite
import sys
import datetime
from datetime import date

class DAO:
	con = None
	cur = None
	def __init__(self):
		try:
			self.con = lite.connect('twitvis.db')

			self.cur = self.con.cursor()
			self.cur.execute('CREATE TABLE IF NOT EXISTS userTerm(user TEXT, term TEXT)')
			self.cur.execute('CREATE TABLE IF NOT EXISTS termHits(termId INT, date DATE, hits INT)')

		except lite.Error, e:
			print "Error %s:" % e.args[0]
			sys.exit(1)

	def insertHits(self, user, term, hits, inday = date.today()):
		try:
			self.cur.execute("SELECT rowid FROM userTerm WHERE user = ? AND term = ?", (user, term))
			data = self.cur.fetchone()
			if not data:
				self.addTermWatch(user, term)
				self.cur.execute("SELECT rowid FROM userTerm WHERE user = ? AND term = ?", (user, term))
				data = self.cur.fetchone()

			self.cur.execute("SELECT date FROM termHits WHERE termId = ?", str(data[0]))
			existingRows = self.cur.fetchone()
			shouldUpdate = False

			if existingRows:
				for existingRow in existingRows:
					year, month, day = map(int, existingRow.split("-"))
					theday = datetime.date(year,month,day)
					if inday == theday:
						shouldUpdate = True
				
			if shouldUpdate:
				print data[0]
				self.cur.execute("UPDATE termHits SET hits = ? WHERE termId = ? AND date = ?", (hits, str(data[0]), str(inday.isoformat)))
			else:
				print "Inserting"
				self.cur.execute("INSERT INTO termHits VALUES( ?, ?, ? )", (data[0], str(inday.isoformat()), hits))
			self.con.commit()

		except lite.Error, e:
			print "Error inserting %s:" % e.args[0]
			sys.exit(1)

	def getUsersAndTerms(self):
		try:
			self.cur.execute("SELECT * FROM userTerm")
			rows = self.cur.fetchall()
			return rows
		except lite.Error, e:
			print "Error %s:" % e.args[0]
			sys.exit(1)
	def addTermWatch(self, user, term):
		try:
			sql = "INSERT INTO userTerm VALUES ( '{!s}', '{!s}' )".format(user, term)
			print sql
			self.cur.execute(sql)
			self.con.commit()
		except lite.Error, e:
			print "Error %s:" % e.args[0]
			sys.exit(1)
	def getResults(self, user, term):
		try:
			self.cur.execute("SELECT rowid FROM userTerm WHERE user = ? AND term = ?", (user, term))
			data = self.cur.fetchone()
			self.cur.execute("SELECT date, hits FROM termHits WHERE termId = ?", str(data[0]))
			return self.cur.fetchall()
		except lite.Error, e:
			print "Error %s:" % e.args[0]
			sys.exit(1)
	def getAllHits(self):
		try:
			self.cur.execute("SELECT * FROM termHits");
			return self.cur.fetchall()
		except lite.Error, e:
			print "Error %s:" % e.args[0]
			sys.exit(1)
	def closeDatabase(self):
		if self.con:
				self.con.close()

