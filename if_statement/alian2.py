## 5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 53, and write an if-else chain. 
# If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien. 
# If the alien’s color isn’t green, print a statement that the player just earned 10 points. 
# Write one version of this program that runs the if block and another that runs the else block.

alian_color = ['green', 'yellow', 'red']
if 'green' in alian_color:
    print('You just earned 5 point for shooting the alian')
else:
    print('You just earned 10 points')

if 'blue' in alian_color:
    print('you earned infinit life')
else:
    print('you got a 2 bonus points')