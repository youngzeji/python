import filetest

import pytest

def test_add():
    assert filetest.add(4, 5) == 9

def test_sub():
    assert filetest.sub(4, 5) == -1

'''
I will be writing test cases for the functions in the pyhton file called filetest.
Now I import the file that consists of the function that need to be tested that is the filetest.py
Next i will import the pytest module. After that i define a couple of test cases with the addition 
and subtraction functions. Each test case should be named test underscore ad and test underscore sub.
I will use the assert keyword inside these functions bcos test primarily rely on this keyword. it checks
for conditions in your code and expects a boolean value of true or false. When the return value is true 
the test passes when it is false the test fails. After writing the statements for our test I run the test
and I specify the file over which i am going to do the testing. To  do this, open a new terminal and enter 
(py -m pytest test_addition.py). and then run the code

You should note that I used an equality operator here but I could have used less than greater than or 
keywords such as is, in, or, not,in all that matters is that the assert statement gets a boolean value

I can also add multiple assert statements in a single function.

instead of using (py -m pytest test_addition.py) you can use (py.test test_addition.py)
'''
