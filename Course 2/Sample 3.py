# Notice the "w" as the second argument.
# It tells the function to open the (new?) file with a write access
file = open("output/testfile.txt","w") 

# Notice the \n at the end of each write statement.
# This is the newline-character, and creates a new line at its position
file.write("Hello World\n") 
file.write("This is our new text file\n") 
file.write("and this is another line.\n") 
file.write("Why? Because we can.\n")
 
file.close() 
