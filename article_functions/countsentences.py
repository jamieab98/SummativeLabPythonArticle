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