#!/usr/bin/python
#Michael Horstkoetter - This bit of code is trying to combine the codes URLS.py and Read RSS into code that prints out only the links of each RSS's feed.
import feedparser
import numpy

#specificUrlName = []
urls = []
ListUrls = []

x = 0

FN = ['FoxNews', 'http://feeds.foxnews.com/foxnews/latest', "'links': [{'href': u'"] #could be 'link' indicates unique feature of source article url
CN = ['CNN', 'http://rss.cnn.com/rss/cnn_topstories.rss', 'feedburner_origlink'] #array holds name, rss url, and key.
rssURL = [FN, CN]

#outPutTypes = ['Instance ID', 'Instance URL', 'Source Name', 'Author', 'Publish Date', 'Body', 'Photos', 'Video', 'audio', 'etag']

for i in range(len(rssURL)): 
	specificUrlName = []
	specificUrlName.insert(i, rssURL[i][0])			#good - Grabs the first names of the RSS feed
	
	feed = feedparser.parse(rssURL[i][1])			#good - Parses the code, so it is now deciferable to numpy
	numberUrls = str(feed).count(rssURL[i][2]) 		#good - Gives the code the correct Str ID to find the URLs in the raw RSS download. And find the Number of URLS.

	ListUrls = numpy.append(ListUrls, specificUrlName)	#Adds the name of the URL before all of the urls
	listNumUrls = numpy.arange(numberUrls)				#good - Give the while loop something it can play with instead of intergers. It don't like ints. :(

	while x <= (numberUrls-3) :						#good - Loops through to grab each url
		urls = feed.entries[x].links[0].href		#good - Finds each key in each specific url.
		ListUrls = numpy.append(ListUrls, urls)		#good - Places each url in an array.
		x = x + 1									#good - counts up through url in the feed
	print(ListUrls)									#good - prints to screen to verify

	#print(specificUrlName)



