my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print ("My favourite food are:")
print (my_foods)

print ("\nMy friend's favourite foods are:")
print (friend_foods)


my_foods = ['pizza', 'falafel', 'carrot cake']

friend_foods = my_foods[:]

my_foods.append ('cannoli')
friend_foods.append ('ice cream')
print ("My favourite food are:")
print (my_foods)

print ("\nMy friend's favourite foods are:")
print (friend_foods)


my_foods = ['pizza', 'falafel', 'carrot cake']

# This does not work:
friend_foods = my_foods

my_foods.append ('cannoli')
friend_foods.append ('ice cream')
print ("My favourite food are:")
print (my_foods)

print ("\nMy friend's favourite foods are:")
print (friend_foods)