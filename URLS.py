#!/usr/bin/python
#Michael Horstkoetter - This bit of code is trying to find all the new URLs for articles on each RSS Feed listed keeping a continuously updated list.

import feedparser

e = []

FN = ['FoxNews', 'http://feeds.foxnews.com/foxnews/latest', "'links': [{'href': u'"] #could be 'link' indicates unique feature of source article url
CN = ['CNN', 'http://rss.cnn.com/rss/cnn_topstories.rss', 'feedburner_origlink']
rssURL = [FN, CN]

outPutTypes = ['Instance ID', 'Instance URL', 'Source Name', 'Author', 'Publish Date', 'Body', 'Photos', 'Video', 'audio', 'etag']

#Find the latest articles and store them ontop of the other stored articles
#firstURL = outPutTypes[1]
#for i in 

for i in range(len(rssURL)): 
	d = feedparser.parse(rssURL[i][1])
	e.insert(i, rssURL[i][0])
#	While  
#		f = d.entries[1].link
	


	#for i in range(len(outPutTypes)):
	print(d)