import os
import urllib2

from flask import Flask, request


app = Flask(__name__)

@app.route("/")
def echo():
	data = urllib2.unquote(request.query_string)
	if ' ' not in data:
		return data.replace('+', ' ')
	else:
		return data

if __name__ == '__main__':
	debug = os.getenv("DEBUG", True)
	port = int(os.environ.get('PORT', 5000))
	app.run(
		debug=debug,
		host="0.0.0.0",
		port=port,
	)
