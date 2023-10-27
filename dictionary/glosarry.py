## 6-3. 
# Glossary: A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let’s call it a glossary. 
# Think of ﬁve programming words you’ve learned about in the previous chapters. 
# Use these words as the keys in your glossary, and store their meanings as values. 
# Print each word and its meaning as neatly formatted output. 
# You might print the word followed by a colon and then its meaning, or print the word on one 
# line and then print its meaning indented on a second line. 
# Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.

glossarys = {'Indent' : 'A white, blank or tab space for code styling',
             'Concatenate' : 'To add, merge or join together',
            'Modify' : 'to change or update',
            'Refference' : 'pointing to memory of a variable',
            'nested' : 'something within the same thing',
            'Iteration' : 'reoccure'
            }

print('Indent :')
print(f"\t{glossarys['Indent']}\n")
print('Concatenate :')
print(f"\t{glossarys['Concatenate']}\n")
print('Modify :')
print(f"\t{glossarys['Modify']}\n")
print('Refference :')
print(f"\t{glossarys['Refference']}\n")
print('nested :')
print(f"\t{glossarys['nested']}")