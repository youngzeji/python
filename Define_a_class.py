'''
This is a stub for a class representing a house that can be used to create objects and evualate different metrics
that we may require in constructing it. 
'''

class House:
    num_rooms = 5
    bathrooms = 2
    def cost_evaluation(self):
        print(self.num_rooms)
        pass


house = House()
print(house.num_rooms)
print(House.num_rooms)

house.num_rooms = 7
print(House.num_rooms)
print(house.num_rooms)

House.num_rooms = 8
print(House.num_rooms)
print(house.num_rooms)