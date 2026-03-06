#Program to search for an element in a list and dictionary using for and if

fruits = ["Apple","Mango","Banana","Orange","Grapes"]
s = input("Search for a fruit to check if it is available : ")
found = False
for i in fruits:
    if(s==i):
        print("Available.")
        found = True
        break
if(not found):
    print("Not available.\n")

student = {"name":"Sudit Shrimali","ID":"BOE11125047"}
data = input("Search for a student name or ID in a dictionary : ")
found = False
for i in student:
    if(i==data):
        found = True
        print(student[i])
if(not found):
    print("Try entering name or ID!")