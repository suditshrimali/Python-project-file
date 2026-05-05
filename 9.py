#Program to demonstrate the use of break, continue, pass, and else in loops

#Use of break
print("Break")
for i in range(0,5):
    if(i==3):
        break
    print(i)

#Use of continue
print("\nContinue")
for i in range(0,5):
    if(i==3):
        continue
    print(i)

#Use of pass
print("\nPass")
for i in range(0,5):
    pass

#Use of else
print("\nelse")
for i in range(0,5):
    print(i)
else:
    print("Done!")