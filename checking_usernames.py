current_users = ['Wole','Kogs','Royce','Sam891','Kentsayy']
new_users = ['Wole','Kogs','Tobi','Sade','Demi']
current_users_lower = [user.lower() for user in current_users]

for user in new_users:
    user_lower = user.lower()
    if user_lower in current_users_lower:
        print("Please enter another username")
    else:
        print("This username is available")