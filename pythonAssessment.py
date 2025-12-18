import string

def count_specific_word(text, word):
    words = text.split()
    count = 0
    i = 0
    while i < len(words):
        w = words[i]
        w_clean = w.lower().strip(string.punctuation + string.whitespace).strip('“”')
        if w_clean == word.lower().strip(string.punctuation + string.whitespace):
            count += 1
        i += 1
    print(count)


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
    
    if text == "":
        most_common = "None"
    print (most_common, word_count)

def calculate_average_word_length(text):
    words = text.split()
    clean_words = []
    for w in words:
        clean_word = w.strip(string.punctuation + string.whitespace + '“”').lower()
        if clean_word == "\ufeff":
            exit
        elif clean_word == "":
            exit
        else:
            clean_words.append(clean_word)
    
    length_list = []
    for word in clean_words:
        length_list.append(len(word))

    total_length = 0
    for length in length_list:
        total_length += length

    if total_length == 0:
        average = 0
    else:
        average = total_length / len(length_list)
    print(average)

def count_paragraphs(text):
    paragraphs = text.split("\n\n")
    if text == "":
        paragraph_count = 1
    else:
        paragraph_count = len(paragraphs)
    print(paragraph_count)

def count_sentences(text):
    sentence_separator = (".", "!", "?")
    sentences = text.split()

    if text == "":
        sentence_count = 1
    else:
        sentence_count = 0

    for sentence in sentences:
        if sentence[-1] in sentence_separator:
            sentence_count += 1
    print(sentence_count)