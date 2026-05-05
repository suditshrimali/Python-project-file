# Program to open a file and read contents using read(), readline() and readlines()

# Open the file in read mode
file = open('example.txt', 'r')
# Read the entire contents of the file
content = file.read()
print("Using read():")
print(content)

# Move the file pointer back to the beginning of the file
file.seek(0)
first_line = file.readline()
print("\nUsing readline():")
print(first_line)
second_line = file.readline()
print(second_line)

# Move the file pointer back to the beginning of the file
file.seek(0)
# Read all lines of the file into a list
lines = file.readlines()
print("\nUsing readlines():")
for line in lines:
    print(line, end='') # end='' is used to avoid adding extra new line characters

# Close the file
file.close()