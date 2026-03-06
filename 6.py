#Program to display all prime numbers within a given range using for loop and range()

n = int(input("Enter a number : "))
for i in range(2,n+1):
    isPrime = True
    for j in range(2,i):
        if(i%j==0):
            isPrime = False
            break
    if(isPrime):
        print(i)