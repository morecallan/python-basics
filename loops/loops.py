magicians = ["alice", "david", "carolina"]

for magician in magicians:
    print(magician.title())

for value in range(1, 5):
    print(value)

even_numers = list(range(2, 11, 2))

for value in even_numers:
    print(value)

squares = []

for value in range(1, 11):
    square = value**2
    squares.append(square)

print(squares)

places_to_visit = ["Disney World", "Harry Potter World", "New Zealand", "Frankfurt", "Banana Stand"]

for place in places_to_visit:
    print("I want to visit " + place)

# List and Simple Stats
for value in range(1, 21):
    print(value)

loads_of_nums = []

for value in range(1, 1000001):
    loads_of_nums.append(value)
# alt: loads_of_nums = list(range(1, 1000001))

print(sum(loads_of_nums))

odd_nums = list(range(1, 20, 2))
for value in odd_nums:
    print(value)

in_threes = list(range(3, 30, 3))
for value in in_threes:
    print(value)

to_ten = list(range(1,10))
for value in to_ten:
    print(value ** 3)

list_generation = [value ** 3 for value in range(1,10)]
print(list_generation)


# SLICING AND STUFF
print("These are the first 3 items in the list:")
for value in places_to_visit[:3]:
    print(value)

print("These are the middle 3 items in the list:")
for value in places_to_visit[1:4]:
    print(value)

print("These are the last 3 items in the list:")
for value in places_to_visit[-3:]:
    print(value)

# My Pizza, Your Pizzas
my_pizzas = ["Pepperoni", "Cheese", "Pineapple", "Hawaiian", "Meat Lover"]
friends_pizzas = my_pizzas[:]

my_pizzas.append("Anchovie")
friends_pizzas.append("Hamburger")

print("My favorite pizzas are:")
for value in my_pizzas:
    print(value)

print("My friends favorite pizzas are:")
for value in friends_pizzas:
    print(value)
