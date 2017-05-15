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
