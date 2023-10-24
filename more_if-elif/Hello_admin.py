## 5-8. 
# Hello Admin: Make a list of ﬁve or more usernames, including the name 'admin'. 
# Imagine you are writing code that will print a greeting to each user after they log in to a website. 
# Loop through the list, and print a greeting to each user. 
# If the username is 'admin', print a special greeting, such as Hello admin, would you lik e to see a status report? 
# Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again.

username = ['Mark', 'Elon', 'Admin', 'Jaden', 'Martins']
for name in username:
    if name == 'Admin':
        print('Hello Admin, would you like to see a status report!')
    else:
        print(f'Hello {name} thank you for logging in again')
