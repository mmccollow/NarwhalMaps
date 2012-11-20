#!/usr/bin/env python

from flask import Flask

app = Flask(__name__)

@app.route('/')
def slideshow():
	pass

if __name__ == '__main__':
	app.run()

