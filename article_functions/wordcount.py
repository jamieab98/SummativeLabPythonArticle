import string

def count_specific_word(text, word):
    words = text.split()
    count = 0
    for w in words:
        w_clean = w.lower().strip(string.punctuation + string.whitespace).strip('“”')
        if w_clean == word.lower().strip(string.punctuation + string.whitespace):
            count += 1
    print(count)
