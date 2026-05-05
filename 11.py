# Program to define,slice, and perform operations on lists and nested lists

#Defining a list
fruits = ["Apple","Mango","Banana","Orange","Grapes"]
print("List of fruits : ",fruits)

#Slicing a list
print("Slicing the list from index 1 to 3 : ",fruits[1 : 4])

#Defining a nested list
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print("Nested list (matrix) : ",matrix)

#Accessing elements in a nested list
print("Element at row 1, column 2 : ",matrix[0][1])

#Slicing a nested list
print("Slicing the first two rows of the matrix : ",matrix[0 : 2])

#List operations

#Concatenation
list1 = [1,2,3]
list2 = [4,5,6]
list3 = list1 + list2
print("Concatenated list : ",list3)

#Repetition
list4 = list1 * 2
print("Repeated list : ",list4)

#Membership
print("Is 2 in list1? ",2 in list1)
print("Is 5 in list1? ",5 in list1)

#Comparison
print("Is list1 equal to list2? ",list1 == list2)
print("Is list1 equal to [1,2,3]? ",list1 == [1,2,3])