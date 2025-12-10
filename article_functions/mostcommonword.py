import string

def identify_most_common_word(text):
    word_counts = {}
    logged_words = []
    words = text.split()

    for w in words:
        w_clean = w.lower().strip(string.punctuation + string.whitespace).strip('“”')
        if w_clean in logged_words:
            word_counts[w_clean] = word_counts[w_clean] + 1
        else:
            logged_words.append(w_clean)
            word_counts[w_clean] = 1
    
    most_common = ""
    word_count = 0
    for word in word_counts:
        if word_counts[word] > word_count:
            most_common = word
            word_count = word_counts[word]
    print (most_common, word_count)
