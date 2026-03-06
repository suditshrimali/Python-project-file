#Program using while loop to find factorial of a number

n = int(input("Enter a whole number : "))
fact = 1
i = 2
while(i<=n):
    fact *= i
    i += 1
if(n<0):
    print("Try a whole number!")
else:
    print("Factorial of",n,"=",fact)