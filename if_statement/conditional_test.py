boy = 'Obi'
girl = 'Ada'

if girl == 'ada':
    print("True")
else:
    print("False")

if boy != 'Ada':
    print('True')
else:
    print('False')

# Tests using the lower() method
if girl.lower() == 'Ada':
    print("True")
else:
    print("False")

# Tests using the and keyword and the or keyword
min_score = 70
max_score = 150

obi = 80;
ada = 20;

if ada <= min_score or ada > min_score:
    print('Passed!')
else:
    print('Failed')

if obi > min_score and obi < max_score:
    print('passed')

# Test whether an item is in a list

class_bnames = ['John', 'Ruth', 'Emma', 'Mark']
if 'Grace' in class_bnames:
    print('Present')
else:
    print('Absent')

# Test whether an item is not in a list

class_bnames = ['John', 'Ruth', 'Emma', 'Mark']
if 'Grace' not in class_bnames:
    print('Not included')
else:
    print('Is among')