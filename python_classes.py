class MyClass:
    a = 5
    print("Hello")

    def hello(self):
        print("hello, world")
   

#create an object for the class MyClass
myclass = MyClass()
print(MyClass.a)
print(myclass.a)
print(myclass.hello())
