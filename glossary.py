prog_words = {
    'print':'print out whatever is enclosed in the parenthesis',
    'int':'type cast whatever is in the parenthesis to an integer data type',
    'if-else':'perform an action based on whether an expression evaluates to True or False',
    'for':'Loop through all them items in a python object',
    'list':'Returns a list using whatever is in the parenthesis as its items'
    }

'''for word in prog_words:
    message = "\n" + word + ": " + prog_words[word] + "\n"
    print(message)'''
    
for word in prog_words.keys():
    message = "\n" + word + ": " + prog_words[word] + "\n"
    print(message)