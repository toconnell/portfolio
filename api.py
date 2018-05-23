#!/usr/bin/python3

#
#	flask
#

from flask import Flask, Response, redirect
from flask_cors import CORS

#
#	std lib
#
from bson import json_util
import json
import ssl

#
#	private
#

import settings


#
#	app starts here!
#

application = Flask(__name__)
CORS(application)

#
#	routes
#

# redirect for all posts shorthand
@application.route('/posts', methods=['GET'])
def all_posts():
	return redirect('/posts/0', code=302)

# retrieve a number of posts in reverse chron
@application.route('/posts/<count>', methods=['GET'])
def posts(count):
	try:
		count = int(count)
	except:
		return Response(response='In /posts/[count]; requests, [count] must be an integer!', status=400)

	if count == 0:
		posts = settings.mdb.posts.find({'published': True}).sort('created_on', -1)
	else:
		posts = settings.mdb.posts.find({'published': True}).sort('created_on', -1).limit(count)

	return Response(
		response=json.dumps(list(posts), default=json_util.default),
		status=200,
		mimetype="application/json"
	)



#
#	__main__
#

if __name__ == '__main__':
	context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
	context.load_cert_chain(
		'/etc/letsencrypt/live/toconnell.info/fullchain.pem',
		'/etc/letsencrypt/live/toconnell.info/privkey.pem',
	)
	application.run(
		host=settings.get('api','host'),
		port=settings.getint('api','port'),
		debug=settings.getboolean('api','debug'),
		ssl_context=context
	)



