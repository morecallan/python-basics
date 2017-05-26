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
