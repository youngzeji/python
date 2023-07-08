class A:
    def a(self):
        return "Function inside A"
    
class B:
    def a(self):
        return "Function inside B"
    
class C(B,A):
    pass

c = C()
print(c.a())

'''
class C inherits from classes B and A. When I dont find any function a()inside class C, I should search
for classes B and A its important that i do it in that order.
'''