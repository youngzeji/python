import sys
locations = sys.path
print(locations)

for i in locations:
    print(i)

'''
Its always a good practice to import all the required modules right at the beginning. 
I will import a built-in module called calendar. I will now use a couple of functions that the calendar has.
I will use a function called leapdays, which has two inputs, year 1 and year 2, and it will be returning
another integer value. So what i am going to do is write the leapdays function, write to input years and 
return the value in a variable called leap days. I am going to print the value of a variable. I get a return
value of 13 leap days btw 2000 and 2050.

Use another function. This function is called isleap. It takes one of the years as an input and returns a
Boolean value. It tells you if a given year is a leap year.
'''

import calendar

leapdays = calendar.leapdays(2000, 2050)
print(leapdays)


isitleap = calendar.isleap(2036)
print(isitleap)