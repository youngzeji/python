# lets demonstrate how to create a class and instantiate it with variables and methods then referencing
# the same variables and methods in separate instances to yield different outcomes.

class Recipe():
    def __init__(self, dish, items, time) -> None:
        self.dish = dish
        self.items = items
        self.time = time

    def content(self):
        print("The " + self.dish  + " has" + str(self.items) + \
              " and takes " + str(self.time) + " min to prepare")

pizza = Recipe("pizza", ["chesse", "Bread", "tomato"], 45)
pasta = Recipe("pasta", ["penne", "sauce"], 55)

print(pizza.items)
print(pasta.items)

print(pizza.content())
