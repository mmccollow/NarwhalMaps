#!/usr/bin/env python

from BeautifulSoup import BeautifulSoup as BS
import urllib2
import urlparse
import re

SOURCE_URL = "http://www.reddit.com/r/MapPorn/top/?sort=top&t=week"

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
		url = link.attrMap['href']
		url_parts = urlparse.urlsplit(url)
		if re.match('^.+\.imgur\.com', url_parts.netloc): # we only want to show images hosted on imgur
			if url[-4:] != '.jpg': # make sure we're pulling the image, not the HTML page
				url += '.jpg'
			href = url 
			title = link.text
			output.append({'title': title, 'href': href})
	return output

