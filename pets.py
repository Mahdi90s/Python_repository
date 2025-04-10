pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print (pets)

while 'cat' in pets:
    pets.remove('cat')
print (pets)
#------------------------------------------------------------------------------
def describe_pet (animal_type, pet_name):
    """Display information about a pet."""
    print (f"\nI have a {animal_type}.")
    print (f"My {animal_type}'s name is {pet_name.title()}.")
    
describe_pet ('hamster', 'harry')
describe_pet ('dog', 'willie')
#------------------------------------------------------------------------------
def describe_pet (animal_type, pet_name):
    """Display information about a pet."""
    print (f"\nI have a {animal_type}.")
    print (f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet (animal_type='hamster', pet_name='harry')
#------------------------------------------------------------------------------
def describe_pet (animal_type, pt_name):
    """Display information about a pet."""
    print (f"\nI have a a {animal_type}.")
    print (f"My {animal_type}'s name is {pet_name.title()}.")
    
describe_pet()