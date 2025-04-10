name = input ("Please enter your name:")
print (f"\nHello, {name}!")
#------------------------------------------------------------------------------

prompt = "If you share your name, we can personalize the massages you see."
prompt += "\nWhat is your first name? "

name = input (prompt)
print (f"\nHello, {name}!")
#------------------------------------------------------------------------------
def greet_user(username):
    """Display a simple greeting."""
    print (f"Hello, {username.title()}!")
    
greet_user('micheal')

#------------------------------------------------------------------------------
def get_formatted_name (first_name, lasst_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {lasst_name}"
    return full_name.title()
# This is an infinite loop
while True:
    print ("\nPlease tell me your name:")
    f_name = input ("First name:")
    l_name = input ("last name:")

    formatted_name = get_formatted_name (f_name , l_name)
    print (f"\nHello, {formatted_name}!")
#------------------------------------------------------------------------------
# quit door
def get_formatted_name (first_name, lasst_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {lasst_name}"
    return full_name.title()

while True:
    print ("\nPlease tell me your name:")
    print ("(enter 'q' at any time to quit)")
    f_name = input ("First name:")
    if f_name == 'q':
        break
    l_name = input ("last name:")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name (f_name , l_name)
    print (f"\nHello, {formatted_name}!")
    
