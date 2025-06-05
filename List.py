List = [1, "Neethu", 5, 7, 9]

print(List[0]) , # List is a data type, that can have multiple data types
print(List[-1]) , #-1 is used to print last index
print(List[0:4]), # is used to print the values from 0 to 4 values at a time

# to insert a command in the List

List.insert(2, "Sharma")
print(List)

# updating the values

List[1] = "NEETHU"
print(List)

List.append("End")
print(List)

# deleting values in the list.

del List[1]
print(List)

#--------------------------------------------------------------------------------------------------------------------

list1 = [1, 1, 2,  4, 5, 7]

print(list1)

list1.insert(4,"Live")
print(list1)

list1.append("smoothend")
print(list1)

list1.insert(1,"common")
print(list1)

del list1[0]
print(list1)

print(list1[1:6])
#-----------------------------------------------------------------------------------------------------------------------