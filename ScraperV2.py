#!/usr/bin/python
#Michael Horstkoetter - This bit of code checks to see of a page has been updated with new articles, and if so get them.

import feedparser
import schedule
from schedule import time
from time import mktime

a = []

#rss source links
FN = ['FoxNews', 'http://feeds.foxnews.com/foxnews/latest']
CN = ['CNN', 'http://rss.cnn.com/rss/cnn_topstories.rss']
RT = ['Reuters', 'http://feeds.reuters.com/reuters/topNews']
NT = ['NewYork Times', 'http://www.nytimes.com/services/xml/rss/nyt/HomePage.xml']
rssURL = [FN, CN, RT, NT]

#Preloads an array for comparring if new arrticles have been posted
for i in range(len(rssURL)): 
    d = feedparser.parse(rssURL[i][1])
    c = time.mktime(d.modified_parsed)
    a.insert(i, c)
#print(a)

#Finds whom has posted new articles!
def job():
    for i in range(len(rssURL)):
        d = feedparser.parse(rssURL[i][1])
        c = time.mktime(d.modified_parsed)
        current_time = time.localtime()
        if a[i] != c:
        	Update = 'NEW INSTANCE posted to ' + rssURL[i][0] + '. - ' + time.strftime('%Y %b %d, %a %H:%M:%S CT', current_time)
        else:
        	Update = 'Nothing new posted to ' + rssURL[i][0] + '. - ' + time.strftime('%Y %b %d, %a %H:%M:%S CT', current_time)
        print(Update)
#        print(c)
#        print(a[i])

        a[i] = c

#It'll be X min (below) untill it starts iterating through the possibilities.
schedule.every(1).minutes.do(job)
#schedule.every().hour.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
