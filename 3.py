#Program to demonstrate Python indentation and code blocks

#Basic block
x = 10
y = 20

def add(a,b):
    #Function block
    result = a + b
    return result

#Conditional blocks
if(x>5):
    #True block
    print("True block")
else:
    #False block
    print("False block")

for i in range(3):
    #Loop block
    print("Inside loop")
    if(i==2):
        #Nested block
        print("Inside nested block")

