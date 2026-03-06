#Program to find the largest of three numbers using nested if-else

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))
if(a>b):
    if(a>c):
        print(a,"is largest out of three given numbers.")
    else:
        print(c,"is largest out of three given numbers.")
elif(b>c):
    print(b,"is largest out of three given numbers.")
else:
    print(c,"is largest out of three given numbers.")