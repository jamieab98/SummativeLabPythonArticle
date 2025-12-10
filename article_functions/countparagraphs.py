def count_paragraphs(text):
    paragraphs = text.splitlines()
    paragraph_count = 1
    ticker = 0

    for paragraph in paragraphs:
        if paragraph == "":
            ticker += 1
        elif paragraph != "":
            ticker = 0
        if ticker == 2:
            ticker = 0
            paragraph_count += 1
    print(paragraph_count)