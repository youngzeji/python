import numpy as np

a = np.zeros(10)
print(a)

b = np.full((2,10), 0.7)
print(b)

c = np.linspace(0,25,7)
print(c)

print(type(c))

'''
The Zeros() function inside numpy creates an array with n number of zeroes inside it.
The full() function creates a two dimensional matrix of dimensions 2*10 consisting only of the values 0.7
linspace() function divides the values between 0 and 25 in 7 equal parts.

Finally, When you see the data type of c, it is special data-type created and used in numpy called as 
ndarray. if you try the output for a and b, it will also be ndarray as numpy deals exclusively with ndarray,
which is a substitute for lists and is far more efficient.
'''

import pandas as pd

d = pd.DataFrame({"Animals": ["Dog", "Cat", "Lion", "Cow", "Elephant"],
                 "Sounds": ["Barks", "Meow", "Roars", "Moo", "Trumpet"]})

print(d)
print(d.describe())

e = pd.DataFrame({"Letters": ["a", "b", "c", "d", "e", "f"],
                  "Numbers": [12, 7, 9, 3, 5, 1]})

print(e.sort_values(by="Numbers"))

e = e.assign(new_values = e["Numbers"]*3)
print(e)


'''
The first output is for the DataFrame called a that displays the ouput in a very systematic format.
The second output uses the describe() function in pandas that will give the count, frequency, top values
and frequency among other values.
In the second DataFrame, b consists of letters and numbers in random order.
The third output is a sorting function that will provide a sorted table leading to shuffling of the data
entries in the table.
lastly, the assign() function takes the values present inside the table, performs an operation over them 
and creates a new variable called new_values that is then added to the table
'''

