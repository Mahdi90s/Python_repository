
# class Stack:
#     def __init__(self):
#         self.items = []
        
#     def is_empty(self):
#         # return self.items == 0
#         return not self.items # more systematic method
    
#     def push(self, item):
#         self.items.append(item)
        
#     def pop(self):
#         self.items.pop()
        
#     def peek(self):
#         return self.items[-1]
    
#     def size(self):
#         return len (self.items)
    
#     def __str__(self):
#         return str(self.items)
    
# if __name__ == "__main__":
#     s = Stack()
#     print(s)
#     print(s.is_empty())
#     s.push(3)
#     print(s)
#     s.push(7)
#     s.push(5)
#     print(s)
#     print(s.pop())
#     print(s)
#     print(s.pop())
#     print(s)
#     s.push(7)
#     s.push(5)
#     print(s.peek())
#     print(s.size())
    
    
    
#-------------------------------------------------------------------------------    
# Python code​​​​​​‌‌​‌​‌​‌‌‌‌​‌​‌‌‌​​​‌​‌‌‌ below
# # You will need this class for your solution. Do not edit it.
# class Stack2:
#     def __init__(self):
#         self.items = []

#     def is_empty(self):
#         # return len(self.items) == 0
#         return not self.items

#     def push(self, item):
#         self.items.append(item)

#     def pop(self):
#         return self.items.pop()

#     def peek(self):
#         return self.items[-1]

#     def size(self):
#         return len(self.items)

#     def __str__(self):
#         return str(self.items)

# # Complete the function definition for reverse_string.
# # Use print("messages...") to debug your solution.

# def reverse_string(my_string):
#     # Use the "accumulator pattern."
#     # Start with an "empty bucket" of the right data type,
#     # and build the solution by filling the bucket within a loop.
#     reversed_string = ""

#     # Create a new stack
#     my_stack = Stack2()
#     # Iterate through my_string and push the characters onto the stack
#     for i in my_string:
#         my_string.push(i)
#     # Use a while loop with the exit condition that the stack is empty.
#     # Within this loop, update reversed_string with characters popped off the stack.
#     while not my_stack.is_empty():
#         reverse_string +=my_stack.pop()
#     # Return the result
#     return reversed_string
#------------------------------------------------------------------------------
def read_maze(file_name):
    """
    Reads a maze stored in a text file and returns a 2d list containing the maze representation.
    """
    try:
        with open(file_name) as fh:
            maze = [[char for char in line.strip("\n")] for line in fh]
            num_cols_top_row = len(maze[0])
            for row in maze:
                if len(row) != num_cols_top_row:
                    print("The maze is not rectangular.")
                    raise SystemExit
            return maze
    except OSError:
        print("There is a problem with the file you have selected.")
        raise SystemExit


if __name__ == "__main__":
    maze = read_maze("mazes/modest_maze.txt")
    for row in maze:
        print(row)

    print("\n--------------------\n")

    maze = read_maze("mazes/challenge_maze.txt")
    for row in maze:
        print(row)