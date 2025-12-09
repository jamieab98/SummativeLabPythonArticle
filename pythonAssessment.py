import string
from article_functions import count_specific_word

with open("news_article.txt", "r") as f:
    article = f.read()
sample = 'Peter apple snapple apple.'

count_specific_word(article, "apple")