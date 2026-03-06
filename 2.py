#program to use different types of operators
a = 32
b = 13
print("a = ",a,",b = ",b)
print("\nArithmetic operators : \n")
print("a + b =",a+b)
print("a - b =",a-b)
print("a * b =",a*b)
print("a / b =",a/b)
print("a ** b =",a**b)
print("a // b =",a//b)
print("a % b =",a%b)

print("\nRelational operators : \n")
print("Is a > b,",a>b)
print("Is a < b,",a<b)
print("Is a <= b,",a<=b)
print("Is a >= b,",a>=b)
print("Is a == b,",a==b)
print("Is a != b,",a!=b)

print("\nLogical operators : \n")
print("Is (a>b) and (a<b),",(a>b) and (a<b))
print("Is (a>b) or (a<b),",(a>b) or (a<b))
print("Is not (a>b),",not(a>b))

print("\nBitwise operators : \n")
print("a & b = ",a&b)
print("a | b = ",a|b)
print("a ^ b = ",a^b)
print("~a = ",~a)
print("a>>2 = ",a>>2)
print("a<<2 = ",a<<2)

print("\nIdentity operators : \n")
print("a is b = ",a is b)
print("a is not b = ",a is not b)

print("\nMembership operators : \n")
l = ["Red","White","Orange"]
print("l =",l)
print("Is 'Red' in l,",'Red' in l)
print("Is 'Orange' not in l,",'Orange' not in l)