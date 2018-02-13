import feedparser

from flask import Flask,render_template

app = Flask(__name__)

RSS_FEEDS = {'bbc':"http://feeds.bbci.co.uk/news/rss.xml",
             'cnn':'http://rss.cnn.com/rss/edition.rss',
             'fox':'http://feeds.foxnews.com/foxnews/latest'}


@app.route("/")
@app.route("/<publication>")
def get_news(publication='bbc'):
    feed = feedparser.parse(RSS_FEEDS[publication])
    first_article = feed['entries'][0]
    return render_template("home.html",articles = feed['entries'])










if __name__ == "__main__":
    app.run(port=5061,debug=True)
