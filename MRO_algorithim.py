class A:
    pass
class B(A):
    pass
class C(B):
    pass
print(C.mro())
print(help(C))

# class A is the parent class B and C the respective child classes. In other words, B  inherits from
# A and C inherits from B. when I print the return for calling the MRO function over class C the output 
# indeed confirms that this is the order that is followed.
# why is this important ?. Imagine the class A has a variable num with value of five and then class B
# also has a number variable with a value of nine here, the MRO function tells you quickly that class C
# will inherit the nine value from class B.

# The help function provides more detailed output with MRO information at the top. it contains information
# about the data descriptors and types used inside the code.