requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print ("hOLD THE ANCHOVIES!")
    
requested_topping = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_topping:
    print ("adding mushrooms.")
if 'pepperoni' in requested_topping:
    print ("adding pepperoni.")
if 'extra cheese' in requested_topping:
    print ("adding extra cheese.")
    
print ("\nFinshed making your pizza!")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print (f"adding {requested_topping}.")
    
print ("\nFinished making your pizza!") 

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print ("Sorry, we are out of green peppers right now.")
    else:    
        print (f"Adding {requested_topping}.")
        
print ("\nFinished making your pizza!")


requested_toppings = []

if requested_toppings:
    for reqested_topping in requested_toppings:
        print (f"Adding {requested_topping}.")
    print ("\nFinished making your pizza!")
else:
    print ("Are you sure you want a plain pizza?")
    
    
    
available_tappings = ['mushrooms', 'olives', 'green peppers', 'pepperoni',
                      'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_tappings:
        print (f"Adding {requested_topping}.")
    else:
        print (f"Sorry, we don't have {requested_topping}.")
    print ("\nFinished making your pizza!")

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    