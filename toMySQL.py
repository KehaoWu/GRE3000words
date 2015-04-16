#!/usr/bin/python
import MySQLdb
db = MySQLdb.connect("localhost","3000word","","3000word")
cursor = db.cursor()
n = 0
for line in open("3000.txt"):
	line_split = line.split("	")
	word = line_split[0]
	translation = line_split[1]
	translation.strip("\"")
	sql = "INSERT INTO word (w,t) values ('%s','%s')" % (word,translation)
	try:
		cursor.execute(sql)
		db.commit()
		n+=1
	except:
		print word+" error"
		db.rollback()

print "\nINSERT data into record table."
sql = "INSERT INTO record (record,totalCount) values(0,'%d')" % (n)
cursor.execute(sql)
db.commit()

db.close()
