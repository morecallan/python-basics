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

places_to_visit = ["Disney World", "Harry Potter World", "New Zealand"]

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
