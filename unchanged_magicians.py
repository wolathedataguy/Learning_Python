names = ['Houdini','Dynamo','Criss Angel','David Blaine','Magic Babe','Penn & Teller','Franz Harary','Harry Jansen']
new_names = []

def make_great(names):
    for i in range(len(names)):
        names[i] = "The Great " + names[i]
        new_names.append(names[i])
    print(new_names)
    return new_names

def show_magicians(names):
    '''Print the name of each magician'''
    for name in names:
        print(name)
    print("\n")

make_great(names[:])
show_magicians(new_names)
show_magicians(names)