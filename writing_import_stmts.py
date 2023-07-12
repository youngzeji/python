'''
 I will now import the built-in math module by typing import math. Just to make sure works,
 i will use a print statement. Most of the modules that you will come across, especially the built-in
 modules, will not have any print statements, and they will simply be loaded by the interpreter.

 Now that I have imported the math module, i want to use a function inside of it. Lets choose the square 
 root function, sqrt. To do this, I type the words math.sqrt. When I type the word math, followed by the dot,
 a list of functions appears in a drop-down menu and you can select from this list.  
''' 

import math

print("Importing the math module")

root = math.sqrt(9)

print(root)

'''
Instead of importing the entire math module as we did above, there is abetter way to handle this by 
directly importing the square root function inside the scope of the project. This will prevent 
overloading the interpreter by importing the entire math module.
'''

from math import sqrt

root1 = sqrt(64)
print(root1)

'''
An alias is an excellent way of importing different modules. Here I asign an alias called m to the math
module. I do this by typing import math as m. 
'''

import math as m

cosine = m.cos(0)
print(cosine)

'''
An alias can be used for a function thats imported. For example, I can type from math import 
factorial as f to alias the factorial function.
'''

from math import factorial as f

factorial_10 = f(10)
print(factorial_10)

'''
Now what if i want to import all the functions inside a given module? I can use the star(*) as the argument.
The practice of using star is not the best appraoch in certain cases.
'''

from math import *

x = log10(50)
print(x)

'''
Importing packages is very similar to impoprting modules in python. Just like you can have imported 
functions, you could also import variables and classes from a given module. 

'''