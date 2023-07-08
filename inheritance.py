# if class A is the parent class and class B is inheriting from it, then class A is passed inside class B 
# as a parameter. This will allow class B to directly access the attributes and methods inside class A.

class A:
    pass
class B(A):
    pass

# Multiple inheritance
class C:
    a = 1 
class D:
    b = 2
class E(C, D):
    pass

c = E()
print(c.a, c.b)

# Multi-level inheritance
class F:
    d = 1
class G(F):
    d = 2

class H(G):
    pass

e = H()
print(e.d)

