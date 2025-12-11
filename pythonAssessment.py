import string
from article_functions import count_specific_word, identify_most_common_word, calculate_average_word_length, count_paragraphs, count_sentences

with open("news_article.txt", "r") as f:
    article = f.read()
sample = 'Peter apple snapple apple.'

#count_specific_word(article, "apple")
#identify_most_common_word(article)
#calculate_average_word_length(article)
#count_paragraphs(article)
count_sentences(article)