# Program to write test into a file using write() and writelines()

# Open the file in write mode
file = open('example.txt', 'w')
# Write a string to the file using write()
bufferLn = input("Enter a line to write to the file: ")
file.write(bufferLn + '\n')

# Write multiple lines to the file using writelines()
lines = []
for i in range(3):
    bufferLn = input("Enter another line to write to the file: ")
    lines.append(bufferLn + '\n')
file.writelines(lines)
file.close()