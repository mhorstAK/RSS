#Code from http://pythonprogramming.net/scraping-parsing-rss-feed/

import urllib2
from urllib2 import urlopen
import re
import cookiejar
#from cookiejar import CookieJar
import time

#if website requires cookies this lets the bot store them
cj = cookiejar
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

#Makes bot look like user on fire fox
opener.addheaders = [('User-agent','Mozilla/5.0')]

#for accepting cookies
def main():
		try:
			page = 'https://www.whitehouse.gov/feed/press'
			sourceCode = opener.open(page).read()
			print sourceCode



		except Exception, e:
			print str(e)

main()
