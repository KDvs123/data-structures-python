heros=['spider man','thor','hulk','iron man','captain america']

# Exercise 2.1

# 1. Length of the list

print("Length of this list is: ", len(heros))

# Exericse 2.2

# 2. Add 'black panther' at the end of this list

heros.append("Black panther")

print("Hero list contains: ", heros)

# Exercise 2.3

# 3. You realize that you need to add 'black panther' after 'hulk',
# so remove it from the list first and then add it after 'hulk'

heros.pop()

heros.insert(3,"Black Panther")

print("Hero list contains: ", heros)

# Exercise 2.4 


# 4. Now you don't like thor and hulk because they get angry easily :)
# So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
# Do that with one line of code.

heros.remove("thor")   
heros[0]="Dr Strange"

# answer for this question

heros[1:3]=['doctor strange']


# Exercise 2.5

# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

heros.sort()

print("Sorted hero list is: ",heros)


