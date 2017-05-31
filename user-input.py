# 7.1 Rental Car

desired_car = input("What car would you like to rent?: \n")
print("Let me see if I can find you a " + desired_car.title() + ".")


# 7.2 Restaurant Seating

num_in_party = input("How many people are in your partay?: \n")
num_in_party = int(num_in_party)

if num_in_party > 8:
    print("You'll have to wait for a table, homies")
else:
    print("We'll get you seated right away.")
