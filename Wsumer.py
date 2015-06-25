import urllib2
from bs4 import BeautifulSoup
import FreqSum
from FreqSum import FrequencySummarizer
import nltk
from nltk.corpus import gutenberg

#def get_only_text(url):
# """ 
#  return the title and the text of the article
#  at the specified url
# """
# page = urllib2.urlopen(url).read().decode('utf8')
# soup = BeautifulSoup(page)
# text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
# return soup.title.text, text

#feed_xml = urllib2.urlopen('http://feeds.bbci.co.uk/news/rss.xml').read()
#feed = BeautifulSoup(feed_xml.decode('utf8'))
#to_summarize = map(lambda p: p.text, feed.find_all('guid'))

a = 'shakespeare-hamlet.txt'
b = 'austen-emma.txt'
c = 'austen-persuasion.txt'
d = 'austen-sense.txt'
e = 'bible-kjv.txt'
f = 'blake-poems.txt'
g = 'bryant-stories.txt'
h = 'burgess-busterbrown.txt'
i = 'carroll-alice.txt'
j = 'chesterton-ball.txt'
k = 'chesterton-brown.txt'
l = 'chesterton-thursday.txt'
m = 'edgeworth-parents.txt'
n = 'melville-moby_dick.txt'
o = 'milton-paradise.txt'
p = 'shakespeare-caesar.txt'
q = 'shakespeare-hamlet.txt'
r = 'shakespeare-macbeth.txt'
s = 'whitman-leaves.txt'

text = nltk.corpus.gutenberg.raw(p)

fs = FrequencySummarizer()
print fs.summarize(text, 1)








#for article_url in to_summarize[:5]:
#  title, text = get_only_text(article_url)
#  print '----------------------------------'
#  print title
#  for s in fs.summarize(text, 2):
#   print '*',s