'''
create a parent class called employees where i will define two variables for first and last names.
create two child classes that both extends the Employee class. the first one is supervisors. 
Modify the init method of the supervisors class so that i can add another variable named password. 
Again, i trigger and select the init method, but this time, it alreday includes the name and last variables.
By calling the employees class, the super method has automatically been applied to access the variables 
there and initialize them within the supervisors class.
I proceed with adding the third variable, password, inside of the init method. then make it can instance 
variable 
'''

class Employees:
    def __init__ (self, name, last) -> None:
        self.name = name
        self.last = last

class Supervisors(Employees):
    def __init__(self, name, last, password) -> None:
        super().__init__(name, last)
        self.password = password

class Chefs(Employees):
    def leave_request(self, days):
        return "May i Take a leave for " + str(days) + " days"
    
adrian = Supervisors("Adrian", "A", "apple")

emily = Chefs("Emily", "E")
Juno = Chefs("Juno", "J")

print(emily.leave_request(3))
print(adrian.password)
print(emily.name)
    

    



'''
I will write another child class called chefs. Again, I extended the employees class by adding employees 
as a method inside the class. I want this one to contain a new function called leave_request, so i type
def leave_request and then self and days as the variables in parentheses. The purpose of the leave_request 
function is to return a line that specifies the number of days requested.

create instances from this class
'''    