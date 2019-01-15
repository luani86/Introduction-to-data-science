import csv

# %precision 2

with open('cars.csv') as csvfile:
    cars = list(csv.DictReader(csvfile))
# print cars[:3]
# print cars[0].keys()

# Average price by color of the car
colors = set(car['color'] for car in cars)
prices_by_color = []
for color in colors:
    price_sum = 0
    colors_count = 0
    for car in cars:
        if car['color'] == color:
            price_sum += float(car['price'])
            colors_count += 1
    prices_by_color.append((color, price_sum / colors_count))
# prices_by_color.sort(key=lambda x: x[1])
# print prices_by_color

###################### Objects
class Person:
    department = 'School of Information' #a class variable

    def set_name(self, new_name): #a method
        self.name = new_name
    def set_location(self, new_location):
        self.location = new_location
pera = Person()
pera.set_name('Pera')
pera.set_location('Belgrade')
print '{} lives in {} and works in the {}'.format(pera.name, pera.location, pera.department)

############ Minimal value
def minimal_value(arr):
    minimum = arr[0]
    for i in arr:
        if i < minimum:
            minimum = i
    return minimum
store_1 = [10.0, 5.0, 20.0]
cheapest = minimal_value(store_1)
print cheapest

###################################### Map ???
store1 = [10.00, 11.00, 12.34, 2.34]
store2 = [9.00, 11.10, 12.34, 2.01]
cheapest = map(min, store1, store2)
for item in cheapest:
    print(item)

################### numpy and iterating over arrays
import numpy as np
mylist = [1, 2, 3]
x = np.array(mylist)
# print type(x)
# print type(mylist)

m = np.array([[7, 8, 9], [10, 11, 12]])
# print m

test = np.random.randint(0, 10, (4,3))
print test
test2 = test**2
print test2

for i, j in zip(test, test2):
    print(i,'+',j,'=',i+j)