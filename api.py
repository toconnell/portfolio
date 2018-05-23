#!/usr/bin/python3

#
#	flask
#

from flask import Flask

#
#	std lib
#


#
#	private
#

import settings


#
#	app starts here!
#

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World! Moved"

if __name__ == '__main__':
    app.run(
		host=settings.get('api','host'),
		port=settings.getint('api','port'),
		debug=settings.getboolean('api','debug')
	)



