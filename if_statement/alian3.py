## 5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an ifelif-else chain. 
# If the alien is green, print a message that the player earned 5 points. If the alien is yellow, 
# print a message that the player earned 10 points. If the alien is red, 
# print a message that the player earned 15 points. 
# Write three versions of this program, making sure each message is printed for the appropriate color alien. 

alian_color = ['green', 'yellow', 'red']
if 'green' in alian_color:
    print('You just earned 5 point for shooting the alian')
elif 'yello' in alian_color:
    print('You just earned 10 points')
elif 'red' in alian_color:
    print('You just earned 15 points')

alian_color = ['green', 'yellow', 'red']
if 'green' in alian_color:
    print('You just earned 5 point for shooting the alian')

if 'yellow' in alian_color:
    print('You just earned 10 point for shooting the alian')

if 'red' in alian_color:
    print('You just earned 15 point for shooting the alian')