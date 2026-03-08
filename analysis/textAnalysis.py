from textblob import TextBlob

with open('myText.txt', 'r') as file:
    text = file.read()

blob = TextBlob(text)
sentiment = blob.sentiment.polarity

print(f"Text: {text}\n")
print("----------------------------------------\n")
print(f"Sentiment polarity: {sentiment}")
