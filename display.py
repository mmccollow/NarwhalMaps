#!/usr/bin/env python

from flask import Flask
import fetch

app = Flask(__name__)

@app.route('/slideshow')
def slideshow():
	data = fetch.toJson(fetch.parse())
	return render_template("slideshow.html", data=data)

if __name__ == '__main__':
	app.run()

