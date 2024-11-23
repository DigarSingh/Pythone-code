'''
Data Types
Numerical 
     - int
     - float
     - complex
Boolean
     - True
     - False
String
'''
print("list")
'''
list
list is a collection of items. It is ordered and changeable. Allows duplicate members.
list is represented by square brackets []
list can have different data types
list can have duplicate values
list can have nested lists
'''

lst= [1,2,3,4,5]
print(lst)
print(type(lst))
print("\n")

#list methods

#append
lst.append(6) #append method is used to add an element at the end of the list
print(lst)
print("\n")

#insert
lst.insert(2,7) #insert method is used to add an element at a specific index
print(lst)
print("\n")

#extend
lst1=[8,9,10]
lst.extend(lst1) #extend method is used to add elements of one list to another list
print(lst)
print("\n")

#index
print(lst.index(7)) #index method is used to find the index of an element
print("\n")

#remove
lst.remove(1) #remove method is used to remove an element from the list
print(lst)
print("\n")

#reverse
lst.reverse() #reverse method is used to reverse the list
print(lst)
print("\n")

#sort
lst.sort() #sort method is used to sort the list
print(lst)
print("\n")

#pop
print(lst.pop()) #pop method is used to remove the last element from the list
print("\n")
print(lst)
print("\n")

#count
print(lst.count(2)) #count method is used to count the number of times an element is present in the list
print("\n")

#clear
lst.clear() #clear method is used to clear the list
print(lst)
print("\n")

#copy
lst= [1,2,3,4,5]
lst1= lst.copy() #copy method is used to copy the list
print(lst1)
print("\n")

#list comprehension
lst= [x for x in range(10)] #list comprehension is used to create a list
print(lst)
print("\n")

#Indexing
print(lst[2]) #indexing is used to get the element at a specific index
print("\n")

#Slicing
print(lst[2:5]) #slicing is used to get the elements from a specific range
print("\n")

#Negative Indexing
print(lst[-1]) #negative indexing is used to get the element from the end of the list
print("\n")

#Negative Sliceing
print(lst[-3:-1]) #negative slicing is used to get the elements from the end of the list
print("\n")


print("tuple")
'''
tuple
tuple is a collection of items. It is ordered and unchangeable. Allows duplicate members.
tuple is represented by round brackets ()
tuple can have different data types
tuple can have duplicate values
tuple can have nested tuples
'''

tup= (1,2,3,4,5)
print(tup)
print(type(tup))
print("\n")

#tuple methods

#index
print(tup.index(3)) #index method is used to find the index of an element
print("\n")

#count
print(tup.count(2)) #count method is used to count the number of times an element is present in the tuple
print("\n")

print("dictionary")
'''
dictionary
dictionary is a collection of items. It is unordered and changeable. No duplicate members.
dictionary is represented by curly brackets {}
dictionary has key value pairs
dictionary can have different data types
dictionary can have duplicate values
dictionary can have nested dictionaries
'''

dic= {1:"one",2:"two",3:"three",4:"four",5:"five"}
print(dic)
print(type(dic))
print("\n")

#dictionary methods

#keys
print(dic.keys()) #keys method is used to get the keys of the dictionary
print("\n")

#values
print(dic.values()) #values method is used to get the values of the dictionary
print("\n")

#items
print(dic.items()) #items method is used to get the key value pairs of the dictionary
print("\n")

#get
print(dic.get(2)) #get method is used to get the value of a key
print("\n")

#pop
print(dic.pop(3)) #pop method is used to remove a key value pair from the dictionary
print("\n")
print(dic)
print("\n")

#popitem
print(dic.popitem()) #popitem method is used to remove the last key value pair from the dictionary
print("\n")
print(dic)
print("\n")

#clear
dic.clear() #clear method is used to clear the dictionary
print(dic)
print("\n")

print("set")
'''
set
set is a collection of items. It is unordered and unindexed. No duplicate members.
set is represented by curly brackets {}
set can have different data types
set cannot have duplicate values
set cannot have nested sets
'''

st= {1,2,3,4,5}
print(st)
print(type(st))
print("\n")

#set methods

#add
st.add(6) #add method is used to add an element to the set
print(st)
print("\n")

#update
st.update([7,8,9]) #update method is used to add multiple elements to the set
print(st)
print("\n")

#remove
st.remove(1) #remove method is used to remove an element from the set
print(st)
print("\n")

#discard
st.discard(2) #discard method is used to remove an element from the set
print(st)
print("\n")

#pop
print(st.pop()) #pop method is used to remove an element from the set
print("\n")
print(st)
print("\n")

#clear
st.clear() #clear method is used to clear the set
print(st)
print("\n")
