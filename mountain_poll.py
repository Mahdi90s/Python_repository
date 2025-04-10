responses = {}
# set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    #prompt for person's name and response.
    Name = input ("\nWhat is your name? ")
    response = input ("which mountain would you lik to climb someday? ")
    # Store the response in the dictionary.
    responses[Name] = response
    # Find out if anyone else is going to take the poll.
    repeat = input ("Would you like to let another person respond? (yes/ no)")
    if repeat == 'NO':
        polling_active = False
    # Polling is complete. Show the results.
    print ("\n--- Poll results ---")
    for name, response in responses.items():
        print (f"{name} would like to clim {response}.")