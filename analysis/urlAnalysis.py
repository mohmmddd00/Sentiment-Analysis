from textblob import TextBlob
from newspaper import Article

url = 'https://www.bbc.com/news/articles/c2k88j5x9wdo'

article = Article(url)
article.download()
article.parse()
article.nlp()

text = article.summary

blob = TextBlob(text)
sentiment = blob.sentiment.polarity # -1 to 1, where -1 is negative and 1 is positive
print(f"Article Title: {article.title}\n")
print("----------------------------------------\n")
print(f"Sentiment polarity: {sentiment}")
