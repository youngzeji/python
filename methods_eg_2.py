class A:
    def b(self):
        return "Function inside A"
    
class B: 
    def b(self):
        return "Function inside B"
class C(A, B):
  #  def b(self):
   #     return "Function inside C"
    pass

class D(C):
    pass

d = D()
print(d.b())

'''
Class D inherits from class C, which in turn inherits from classes A and B. Class D accesses the immediate
superclass of class D, which is class C and resolves the value of the variable once its found in that 
superclass

Now lets comment out the declaration inside class C. And replace it with a pass keyword to keep the code 
functional.
Since there was no value present inside class C either, the function call above would go to A. That is bcos
class C will point to class A as having higher precedence while inheriting.
'''