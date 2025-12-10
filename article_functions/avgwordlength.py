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
    #make a a list of every unique word (repeated words don't matter)

    #iterate through every word in the unique word list and make an new list consisting of the length of each unique word

    #add up all the values (maybe by iterating through the list) and then divide by the number of unique words