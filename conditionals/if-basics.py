# SIMPLE EXAMPLE

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

banned_users = ["andrew", "carolina", "david"]
user = "maria"

if user.lower() not in banned_users:
    print("Yo, " + user.title() + " you're allowed in here.")

people = ['bob', 'FRANK', 'margaret', 'Amanda', 'tASHE']

for person in people:
    for banned in banned_users:
        if person.lower() === banned.lower():
            print("You are banned, " + person)
