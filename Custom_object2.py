# will create a class, define its state by creating variables and functions to define its attributes and 
# behavior, and then instantiate it using some variable. Finally will use the class members 
# to get desired output.

class MyFirstClass():
    print("Who wrote this?")
    index = "Author-Book"

    def hand_list(self, philosopher, book):
        print(MyFirstClass.index)
        print(philosopher + " wrote the book " + book)

whodunnit = MyFirstClass()
whodunnit.hand_list("Sun Tzu", "The Art of War")