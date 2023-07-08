# Imagine a scenario in which an employer wants to collect donations from employees for a charitable cause.
# Lets write some code to make that possible. 
# First I import the ABC module and its abstract method,
# Then i create the employee abstract class called abstractmethod to define a method called donate.Note
# that there is no implementation to this method here.
# After that, I create the class donation which is derived from the abstract class. Note that this class
# overrides the abstractmethod. I write an implementation for the donate function, which takes a user
# inputs, stores it in a variable a, and returns it.
# Next i create two employee instances called john and peter and call the function over them. 
# I also create a lists amounts, to which the returned values will be appended.
# Finally, I have a print statements for amounts which will give the value of the total donations 
# from both employees

 


from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def donate(self):
        pass

class Donation(Employee):
    def donate(self):
        a = input("How much would you like to donate: ")

amounts = []
john = Donation()
j = john.donate()
amounts.append(j)

peter = Donation()
p = peter.donate()
amounts.append(p)

print(amounts)