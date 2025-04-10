message = input ("Tell me something, and I will repeat it back to you:")
print (message)
#------------------------------------------------------------------------------

prompt = "\nTell ,me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

massage = ""
while massage != 'quit':
    massage = input (prompt)
    
    if massage != 'quit':
        print (massage)
#------------------------------------------------------------------------------
prompt = "\nTell something and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

active = True
while active:
    message = input (prompt)
    
    if message == 'quit':
        active = False
    else:
        print (massage)
        