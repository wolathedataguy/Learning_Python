filepath = "gutenberg.txt"

def count_words(word):
    """Counts the number of times a word appears in a body of text"""
    try:
        with open(filepath, encoding='utf-8') as file:
            contents = file.read()
    except FileNotFoundError:
        pass
    else:
        occurence = contents.lower().count(word)
        print(occurence)

count_words('the')