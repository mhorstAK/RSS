#!/usr/bin/python
#Michael Horstkoetter - This bit of code is trying to get all of the atricle URLs from a RSS placed into an array.

import feedparser
import numpy

urls = []
ListUrls = []
i = 0

feed = feedparser.parse('http://feeds.foxnews.com/foxnews/latest')
numberUrls = str(feed).count("'links': [{'href': u'")

listNumUrls = numpy.arange(numberUrls)

while i <= (numberUrls-3) :
	urls = feed.entries[i].links[0].href
	ListUrls = numpy.append(ListUrls, urls)
	i = i + 1
	#print(urls)
print(ListUrls)


#for entry in feed['entries']:
#	content = feed['links']
	#content = urlopen(feed['link']).read()

#print(numberUrls)