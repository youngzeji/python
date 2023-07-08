''' 
create class pay slips and initialize three variables inits called name, pay status and amount.
 I start by typing class pay slips, and then on the next line I call an inits function and then
 select the triggered suggestion. For the variables i type each one in the 
 format self.variable equals variable
''' 
class PaySlips:
    def __init__(self, name, payment, amount) -> None:
        self.name = name
        self.payment = payment
        self.amount = amount
    
    def pay(self):
        self.payment = "yes"

    def status(self):
        if self.payment =="yes":
            return self.name + " is paid " + str(self.amount)
        else:
            return self.name + " is not paid yet"

nathan = PaySlips("nathan", "no ", 1000)
roger = PaySlips("roger", "no ", 3000)

print(nathan.status(), "\n", roger.status())

nathan.pay()
print("After payment")
print(nathan.status(), "\n", roger.status())
        

'''
Create two functions, one to display the status of the payment, another to update the status. The first 
function is written as a def pay with self in parentheses, followed by self.payment equals yes on the next line.
the second function is def status, amd contains an if else statement.

then create an instance of this class for the employee.

also need to make sure to pass these values inside the inits method.

Now call the instant method status to check the status of the payment

The pay function is set up to update the value of the payment variable, 
''' 
    
'''
The two instance objects which are nathan and roger each have their own states. you may have noticed 
that when the instance method pay was called to change the state of nathan, roger was not affected.
this is because the method inside the class is not affected. Rather it provides a separate blueprint 
to each instance, which can be updated for that instance only. 
'''         

