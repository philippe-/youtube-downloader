#!/usr/bin/env python

import re
import sys
import urllib
import urllib2
import requests

from itag import itag_dict

try:
	url = sys.argv[1]
except IndexError:
	print 'Usage: '+sys.argv[0]+' ${YOU_TUBE_URL}'
	sys.exit(0)

URL_RE	= re.compile('url=http')
ITAG_RE	= re.compile('itag=(\d+)')

choice = dict()

def get_itag(text):
	try:
		itag = re.search(ITAG_RE, text).group(0)
		return int(itag.replace('itag=', ''))
	except Exception,e:
		return False

def get_http(url):
	if 'https://' in url:
		url = url[:4]+url[5:]
	return url

def get_links(url):
	return re.split(URL_RE,requests.get(url).content)

def get_title(url):
	raw_title = ''
	title_re = re.compile('.*\<title\>(.*)\<\/title\>.*')
	for line in requests.get(url).content.split('\n'):
		if title_re.match(line):
			raw_title = re.search(title_re, line).group(1)
			return raw_title.replace(' - YouTube', '').replace(' ', '_')

def get_choice(table):
	for i in range(1,len(table)):
		if 'XSRF_REDIRECT_TOKEN' in table[i]:
			pass
		elif 'googlevideo.com' and 'itag' and 'signature' in table[i]:
			itag = get_itag(table[i])
			if itag:
				raw_url	= table[i].split('\\')[0].split(',')[0]
				url		= 'http'+urllib2.unquote(raw_url)
				choice[itag] = url
	return choice

def get_raw(url, title):
	with open(title, 'wb') as handle:
		response = requests.get(url, stream=True)
		if not response.ok:
			print 'Something went wrong'
		for block in response.iter_content(1024):
			if not block:
				break
			handle.write(block)

if __name__ == '__main__':
	title		= get_title(url)
	print title
	url		= get_http(url)
	table		= get_links(url)
	choice	= get_choice(table)
	for itag in choice.keys():
		if itag in itag_dict.keys():
			print str(itag)+' '+itag_dict[itag]
		else:
			print 'new itag found: '+str(itag)
	chosen = int(input())
	if chosen in itag_dict.keys():
		get_raw(choice[chosen], title)
