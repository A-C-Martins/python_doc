## 5-10. 
# Checking Usernames: Do the following to create a program that simulates how websites ensure that everyone has a unique username.
# Make a list of ﬁve or more usernames called current_users. Make another list of ﬁve usernames called new_users. 
# Make sure one or two of the new usernames are also in the current_users list. 
# Loop through the new_users list to see if each new username has already been used. 
# If it has, print a message that the person will need to enter a new username. 
# If a username has not been used, print a message saying that the username is available. 
# Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted. 
# (To do this, you’ll need to make a copy of current_users containing the lowercase versions of all existing users.) 

current_username = ['kate', 'matter', 'andrew', 'philip', 'mark']
new_username = ['AMANDA', 'Mark', 'ANDREW', 'Elon', 'Martins']

validation_list = current_username

for name in new_username:
    if name.lower() in validation_list:
        print('Please enter a new username')
    else:
        print('Username is available')
