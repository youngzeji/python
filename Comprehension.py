# Comprehension in python are a way to create a new sequence from an already existing sequence.
# There are four main types of comprehensions in python: List comprehension, Dictionary comprehension, 
# Set comprhension, Generator comprehension.

# List Comprehension syntax == [<expression> for x in <sequence> if <condition>]
data = [2,3,5,7,11,13,17,19,23,29,31]

#list comprehension: updating the same list
data = [x+3 for x in data]
print("updating the list:", data)

#list comprehension: creating a different list with updated values
new_data = [x*2 for x in data]
print("creating new list:", new_data)

#with an if-condition: Multiples of four:
fourx = [x for x in new_data if x%4 == 0]
print("Divisible by four", fourx)

#Alternatively, we can update the list with the if condition as well
fourxsub = [x-1 for x in new_data if x%4 == 0]
print("Divisible by four minus one:", fourxsub)

#using range function:
nines = [x for x in range(100) if x%9 == 0]
print("nines:", nines)



#Dictionary comprehension syntax = dict = {key: value for key, value in <sequence> if <condition>}

#using range() function and no input list
usingrange = {x:x*2 for x in range(12)}
print("using range()", usingrange)

#lists
months = ["jan", "feb", "mar", "apr", "may", "june", "aug", "sep", "oct", "nov", "dec"]
number = [1,2,3,4,5,6,7,8,9,10,11,12]

#using one input list
numdict = {x:x**2 for x in number}
print("using one input list to create dict:", numdict)

#using two input lists
months_dict = {key:value for (key, value) in zip(number, months)}
print("using two lists:", months_dict)


#set comprehension deals with the set data type and its very similar to list comprehension
#the only key difference is using curly brackets