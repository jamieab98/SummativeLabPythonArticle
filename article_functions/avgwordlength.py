import string
def calculate_average_word_length(text):
    #iterate through every word in the text and turn them into their pure string form
    words = text.split()
    clean_words = []
    for w in words:
        clean_word = w.strip(string.punctuation + string.whitespace + '“”').lower()
        if clean_word == "\ufeff":
            exit
        elif clean_word == "":
            exit
        elif clean_word not in clean_words:
            clean_words.append(clean_word)
    
    length_list = []
    for word in clean_words:
        length_list.append(len(word))
    print (length_list)


    #make a a list of every unique word (repeated words don't matter)

    #iterate through every word in the unique word list and make an new list consisting of the length of each unique word

    #add up all the values (maybe by iterating through the list) and then divide by the number of unique words