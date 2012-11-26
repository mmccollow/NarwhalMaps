#!/usr/bin/env python

from BeautifulSoup import BeautifulSoup as BS
from urllib2 import Request, urlopen as open_url
from urlparse import urlsplit as split_url
import re
from os import listdir, remove

SOURCE_URL = "http://www.reddit.com/r/MapPorn/top/?sort=top&t=week"
HEADERS = {'User-Agent' : 'Mozilla/5 (Linux i386) Gecko'}

def fetch_new_images():
	html = _fetch()
	posts = html.findAll('a', 'title')
	new_images = []
	for post in posts:
		url = post.attrMap['href']
		url_parts = split_url(url)
		if re.match('^.+\.imgur\.com', url_parts.netloc): # we only want to pull images from imgur
			if url[-4:] not in ['.jpg', '.png']: # make sure we're pulling the image, not the HTML page
				continue
			new_images.append({'title': post.text, 'href': url})
	_cache_images(new_images)
	return new_images 

def _fetch():
	request = Request(SOURCE_URL, headers=HEADERS)
	response = open_url(request)
	page_content = response.read()
	soup = BS(page_content)
	return soup

def _cache_images(new_images):
	for image in new_images:
		new_filename = _get_filename_from_url(image['href'])
		request = Request(image['href'], headers=HEADERS)
		response = open_url(request)
		extracted_jpeg_data = response.read() 
		f = open('static/images/' + new_filename, 'wb') #FIXME: catch exceptions?
		f.write(extracted_jpeg_data)
		f.close()
	_purge_everything_but(new_images)

def _purge_everything_but(new_images):
	files_to_keep = set([_get_filename_from_url(image['href']) for image in new_images])
	existing_files = set(listdir('static/images/')) 
	files_to_remove = files_to_keep.difference(existing_files)
	if files_to_remove:
		for file_to_remove in files_to_remove:
			remove('static/images/' + file_to_remove) 

def _get_filename_from_url(url):
	return split_url(url).path.split('/')[-1:][0]
