#!/usr/bin/env python

from flask import Flask
from flask import render_template
import fetch

app = Flask(__name__)

@app.route('/slideshow')
def slideshow():
	links = fetch.fetch_new_images()
	return render_template("slideshow.html", links=links)

if __name__ == '__main__':
	app.run(debug=True)

