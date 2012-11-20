#!/usr/bin/env python

from BeautifulSoup import BeautifulSoup as BS
import urllib
import urllib2

SOURCE_URL = "http://www.reddit.com/r/MapPorn/top/?sort=top&t=day"

def fetch():
	headers = {'User-Agent' : 'Mozilla/5 (Linux i386) Gecko'}
	request = urllib2.Request(SOURCE_URL, headers=headers)
	response = urllib2.urlopen(request)
	page_content = response.read()
	soup = BS(page_content)
	return soup

def parse():
	html = fetch()
	links = html.findAll('a', 'title')
	output = []
	for link in links:
		href = link.attrMap['href']
		title = link.text
		output.append({'title': title, 'href': href})
	return output

