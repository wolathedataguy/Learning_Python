guests = ['Guardiola','Mourinho','Ole','Klopp','Xabi','Carlo','Arteta']
for guest in guests:
    message = guest + ", I would love to have you at my dinner party"
    print(message)

print("\n")
unavailable = "Sadly, " + guests.pop(2) + " won't be coming to the dinner"
print(unavailable)
print("\n")

new_guests = ['Amorin','Motta','Inzaghi']
for new_guest in new_guests:
    guests.append(new_guest)

more_guests = ['Samuel','Olayiwola','Demi']
print("Hello everyone, I found a bigger dinner table. So we can have more guests")
print("\n")

guests.insert(0,'Samuel')
guests.insert((int((len(guests)/2)-1)), 'Olayiwola')
guests.append('Samuel')
for guest in guests:
    message = guest + ", I would love to have you at my dinner party"
    print(message)