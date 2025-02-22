list1= [20,30,'Gaurav'] # defining list
#zero based indexing
# print(list1[0])
list1.append(50)
# print("List :", list1)

# Concatenation, Repeatition, Slicing of data, Membership operator

#Concatenation
list2 = ['Sinha', 60, 70]

concatenated_list = list1 + list2
print(type(concatenated_list))
# print(concatenated_list)
# print("Size of concatenated list",len(concatenated_list)) #Calculating length

#Negative indexing

[20,30,'Gaurav',50, 'Sinha', 60, 70]


# print(concatenated_list[-2])

# Slicing of data

# print(concatenated_list[4:7])  #positive indexes
# print(concatenated_list[-6:-3])  #negative indexes
# print(concatenated_list[0::2])  #slicing data with a skip =>  start:stop:skip

#Repeatition in Lists
list1= [20,30,'Gaurav']
# print(list1*3)


x = 40
# Membership Operation
# if x not in list1:
#     print(f'{x} is not present in list1')
# else:
#     print(f'{x} is present in list1')

# Methods in list - append, extend, insert, remove, pop, clear, count, sort, reverse, copy

# list1.extend(['1','2','3'])
# print(list1)

# list2 = []
#
# print("Enter values to the list")  #User defined input to create a list
# val1 = input()
# list2.append(val1)
# print(list2)


list1= [20,30,'Gaurav',20]
# Insert method
# list1.insert(1,3)  #list.insert(<index>,<value>)
# print(list1)

#remove(<value>) - Remove the first occurence from the list of the specified element
list1.remove(20)
# print("List1 after using remove is :",list1)

# pop(<index>) - pops out the value present at the index, by default it will pop the last value if we don't give any index
popped_item = list1.pop(0)
# print("Popped items from 0th index: ", popped_item)

# print("List1 after pop", list1)


# clear - resets the list
list1.clear()
# print(list1)

list1= [20,30,25,11]

#count(<value>) - counts the occurrences of the specified value
# print(list1.count(20))

# sort - sorts the list in place, by default in ascending order
# list1.sort(reverse=True)
# print(list1)

#copy
# new_list = list1.copy()
# print(new_list)
list1= [20,30,26,12]
# List Comprehension returns a list - [{expression} {iterable} {condition}]
new_list = [x**2 for x in list1 if x%2==0]

# print(new_list)

new_list1 = [x for x in range(6) if x%2!=0]
# print(new_list1)

new_list2 = [ch for ch in 'Bosscoder']
# print(new_list2)


#Nested List - List comprehension

nested_list = [[1,2,3],[4,5,6]]
flattened_list = [list_item for sublist in nested_list for list_item in sublist]

# print(flattened_list)


# Tuples

# What is the difference between a list and a tuple -

# Define a tuple - immutable, fixed size, heterogeneous

tuple1 = (20,30,'Gaurav')

first_element = tuple1[0]
# print(first_element)

# slicing data in tuple
sub_tuple = tuple1[1:]
# print(type(sub_tuple))

# concatenating tuples

tuple2 = (40,50,60)

new_tuple = tuple1 + tuple2

# print(new_tuple)


list_tuples = [(1,2,3),(4,5,6)]

list_tuples[0] = (8,9,10)



print(list_tuples)























