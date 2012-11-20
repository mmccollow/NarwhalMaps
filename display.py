#!/usr/bin/env python

from flask import Flask
import fetch

app = Flask(__name__)

@app.route('/slideshow')
def slideshow():
	links = fetch.toJson(fetch.parse())
	return render_template("slideshow.html", links=links)

if __name__ == '__main__':
	app.run()

