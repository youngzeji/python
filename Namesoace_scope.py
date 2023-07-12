'''
You can view a module as a place where python creates a module object. A module object contains the
 names of different attributes defined inside it. In this way modules are a type of namespace.

LEGB: Local, this is where the first search for a variable is in the local scope. Enclosed this is 
defined inside an enclosing or nested functions. Global is defined at the uppermost level or simply outside
functions, and Built-in, which is the keywords present in the built-in module. In simpler terms, a variable
declared inside a function is local, and the ones outside the scope of any function generally are global.
Here is an example, the outputs for the code onscreen shows the same variable name, Greek, in different scopes. 

A given variable is local, not global when it is declared unless stated otherwise. When a variable is declared 
in a global space, it is also local to that space.

There are two key words that can be used to change the scope of the variables, global and non-local. 
The global keyword helps us access the global variables from within the function. Nonlocal is a special
type of scope defined in python that is used within the nested functions only in the condition that it 
has been defined earlier in the enclosed functions.
'''

def d():
    animal = "elephant"
    def e():
        nonlocal animal
        animal = "giraffe"
        print("inside nested functons: " + animal)

    print("Before calling function: " + animal)
    #e()
    print("After nested function:" + animal)

animal = "camel"
d()
print("Global animal:" + animal)

'''
First the global animal variable gets assigned to camel. Then call thsu function, and once inside it, 
assign elephant to the local animal.Then declare the inner function e and proceed by printing before 
calling functions animal will be the local value which is elephant. Once inside the inner function e,
you use the nonlocal keyword to declare that you are going to use the animal variable and you change the 
value to giraffe, and here you can see that the print statement will give inside nested function the value
of giraffe, which stays consistent even after you get out of the inner function. When you print after 
nested function, the value still remains giraffe. Once the function is fully executed, come out to see that
the value of global animal will be camel which you had assigned at the beginning
'''