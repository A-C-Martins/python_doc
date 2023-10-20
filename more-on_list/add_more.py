dinner_invit = ['Bezus', 'mark', 'Musk']

dinner_invit.insert(0, 'Robert')
dinner_invit.insert(3, 'Nakamoto')
dinner_invit.append('kwik')

suspended_ones = [];


suspended_ones.append(dinner_invit.pop(0))
suspended_ones.append(dinner_invit.pop(1))
suspended_ones.append(dinner_invit.pop(2))
suspended_ones.append(dinner_invit.pop(2))

#Does people suspended for coming for the dinner

print(f"Hello, Mr {suspended_ones[0].title()}, Am sorry, i can't invite you to the dinner any more")
print(f"Hello, Mr {suspended_ones[1].title()}, Am sorry, i can't invite you to the dinner any more")
print(f"Hello, Mr {suspended_ones[2].title()}, Am sorry, i can't invite you to the dinner any more")
print(f"Hello, Mr {suspended_ones[3].title()}, Am sorry, i can't invite you to the dinner any more")
print('\n')
# Those coming for the dinner
print(f"Hello, Mr {dinner_invit[0].title()}, you are still invited to the dinner sir")
print(f"Hello, Mr {dinner_invit[1].title()}, you are still invited to the dinner sir")

# delete the last two invitee
del dinner_invit[0];
del dinner_invit[0];

print(dinner_invit)