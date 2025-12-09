import string

with open("news_article.txt", "r") as f:
    article = f.read()

sample = 'Peter apple snapple apple.'

def count_specific_word(text, word):
    words = text.split()
    count = 0
    for w in words:
        w_clean = w.lower().strip(string.punctuation + string.whitespace).strip('“”')
        if w_clean == word.lower().strip(string.punctuation + string.whitespace):
            count += 1
    return count

result = count_specific_word(article, 'apple')
print(result)