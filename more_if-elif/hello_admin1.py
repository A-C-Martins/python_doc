## 5-9. 
# No Users: Add an if test to hello_admin.py to make sure the list of users is not empty. 
# If the list is empty, print the message We need to ﬁnd some users! 
# Remove all of the usernames from your list, and make sure the correct message is printed. 

username = []
if username:
    for name in username:
        print(f'Hello {name}, Thanks for logging in again')
else:
    print('We need to find some users!')