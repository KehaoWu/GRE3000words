# encoding=utf-8

import os.path
import random
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import MySQLdb

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')


class PoemPageHandler(tornado.web.RequestHandler):
	def get(self):
		db = MySQLdb.connect("localhost","3000word","","3000word")
		cursor = db.cursor()
		cursor.execute("SELECT * FROM record ORDER BY id DESC LIMIT 1;")
		r = cursor.fetchone()
		times = r[0]
		db.commit()
		totalCount = r[2]
		recordID = r[1]
		if recordID == totalCount:
			sql = "INSERT INTO record (record,totalCount) values(0,'%d')" % (totalCount)
			cursor.execute(sql)
			recordID = 0
			times = times + 1
			db.commit()
		sql = "SELECT * from word LIMIT %d,1;" % recordID
		cursor.execute(sql)
		r = cursor.fetchone()
		db.commit()
		def randomAnswer ():
			record_random = random.randint(1,3000)
			sql = "SELECT * from word LIMIT %d,1;" % record_random
			cursor.execute(sql)
			r = cursor.fetchone()[2]
			s = r.split(";")
			db.commit()
			return s[random.randint(0,len(s)-1)]
		answer_set = [randomAnswer(),randomAnswer(),randomAnswer()]
		answer_index = random.randint(0,3)
		correct_answer_t = r[2].split(";")
		correct_answer = correct_answer_t[random.randint(0,len(correct_answer_t)-1)]
		answer_set.insert(answer_index,correct_answer)
		db.close()
		q = r[1]
		a1 = answer_set[0]
		a2 = answer_set[1]
		a3 = answer_set[2]
		a4 = answer_set[3]
		self.render('3000words.html',recordID=recordID, totalCount=totalCount, \
			q=q,times=times,a1=a1,a2=a2,a3=a3,a4=a4,correct=answer_index+1)

	def post(self):
		db = MySQLdb.connect("localhost","3000word","","3000word")
		cursor = db.cursor()
		recordID_new = self.get_argument("ID")
		recordID_new = int(recordID_new) + 1
		sql = "UPDATE record SET record='%d';" % recordID_new 
		cursor.execute(sql)
		db.commit()
		db.close()
		self.get()

if __name__ == '__main__':
	tornado.options.parse_command_line()

	app = tornado.web.Application(
		handlers=[(r'/', IndexHandler), (r'/3000words', PoemPageHandler)],
		template_path=os.path.join(os.path.dirname(__file__), ""),
		static_path=os.path.join(os.path.dirname(__file__), "statics"),
		debug=True
	)
 


	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()

