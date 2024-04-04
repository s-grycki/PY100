# Assume that obj already has a value of 42 when the code below starts running.
# Which of the subsequent statements reassign the variable? Which statements
# mutate the value of the object that obj references? Which statements do neither?
# If necessary, you can read the documentation.

obj = 'ABcd' # Reassignment
obj.upper() # Neither. This method returns a copy but is never reassigned
obj = obj.lower() # Reassignment
print(len(obj)) # Neither. len returns an integer and prints it without saving it
obj = list(obj) # Reassignment (string sequence to list of characters)
obj.pop() # Mutation. Returns last item and removes it from obj
obj[2] = 'X' # Mutation. Changes list without changing where obj points to in memory
obj.sort() # Mutation. Modifies object in place
set(obj) # Neither. This returns a new set object which is never assigned
obj = tuple(obj) # Reassignment (list to tuple)
