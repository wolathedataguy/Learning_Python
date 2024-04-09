def make_shirt(size = 'Large', message = 'I love Python'):
    message = "Your shirt of size " + size + " is going to say " + message + "."
    print(message)

make_shirt('Large')
make_shirt('Medium')
make_shirt(message = 'Python is a great programming language')

#make_shirt(size = 34, message ='This shirt sucks')