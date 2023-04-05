import nltk
from textblob import TextBlob
from newspaper import Article

nltk.download('punkt')

url = "https://www.nytimes.com/2023/01/12/technology/chatgpt-schools-teachers.html"

article = Article(url)

article.download()
article.parse()

article.nlp()

print(f'Title: {article.title}')
print(f'Authors: {article.authors}')
print(f'Publication Date: {article.publish_date}')
print(f'Summary: {article.summary}') 