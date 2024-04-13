names = ['Houdini','Dynamo','Criss Angel','David Blaine','Magic Babe','Penn & Teller','Franz Harary','Harry Jansen']

def show_magicians(names):
    '''Print the name of each magician'''
    for name in names:
        print(name)
    print("\n")

#def make_great():
#    for name in names[:]:
#        current_name = names.pop(0)
#        current_name = "The great " + current_name
#        names.append(current_name)
#    print(names)

def make_great(names):
    for i in range(len(names)):
        names[i] = "The Great " + names[i]

print("Original list of magicians:")
show_magicians(names)

# Modify the list of magicians
make_great(names)

# Show the modified list of magicians
print("\nModified list of magicians:")
show_magicians(names)