usernames = ['admin','Kogs','Royce','Sam891','Kentsayy']
for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?\n")
    elif username:
        print("Hello " + username + ", thank you for logging in again")
if usernames == []:
    print("We need to find some users!")