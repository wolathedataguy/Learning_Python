guests = ['Guardiola','Mourinho','Ole','Klopp','Xabi','Carlo','Arteta']
for guest in guests:
    message = guest + ", I would love to have you at my dinner party"
    print(message)

unavailable = "Sadly, " + guests.pop(2) + " won't be coming to the dinner"
print(unavailable)

new_guests = ['Amorin','Motta','Inzaghi']
for new_guest in new_guests:
    guests.append(new_guest)
print(guests)

for guest in guests:
    message = guest + ", I would love to have you at my dinner party"
    print(message)