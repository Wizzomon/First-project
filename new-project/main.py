import feedparser
feed = input("Please enter your feed URL  ")
data = feedparser.parse(feed)
data.feed.title
print(data.feed.title,"\n", data.feed.description,"\n", data.feed.link)