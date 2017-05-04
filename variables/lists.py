friends = ["leigh", "heather", "marissa", "sarah", "sophie", "megen", "suzy"]

message = "Hey, how's it going, "
print(message + friends[0].title() + "?")
print(message + friends[1].title() + "?")
print(message + friends[2].title() + "?")
print(message + friends[3].title() + "?")
print(message + friends[4].title() + "?")
print(message + friends[5].title() + "?")
print(message + friends[6].title() + "?")

guests = ["tina fey", "amy poehler", "richard simmons"]
message = "Would you like to come to dinner, "
print(message + guests[0].title() + "?")
print(message + guests[1].title() + "?")
print(message + guests[2].title() + "?")

cant_attend = guests.pop(1)
print("Thanks for NOT COMING, " + cant_attend.title() + ".")

guests.insert(1, "richard jones")
print(guests)
print(message + guests[0].title() + "?")
print(message + guests[1].title() + "?")
print(message + guests[2].title() + "?")

message = "Hey, I found a bigger table, so we are going to have a bigger partay! See you there, "
print(message + guests[0].title() + ", " + guests[1].title() + " and " + guests[2].title() + "!")

guests.insert(0, "papa smurf")
guests.insert(2, "albert einstein")
guests.append("henry ford")

message = "Would you like to come to dinner, "
print(message + guests[0].title() + "?")
print(message + guests[1].title() + "?")
print(message + guests[2].title() + "?")
print(message + guests[3].title() + "?")
print(message + guests[4].title() + "?")
print(message + guests[5].title() + "?")

message = ", sorry, bitch, you are uninvited."
uninvited = guests.pop()
print(uninvited.title() + message)
uninvited = guests.pop()
print(uninvited.title() + message)
uninvited = guests.pop()
print(uninvited.title() + message)
uninvited = guests.pop()
print(uninvited.title() + message)

message = ", you are still invited to dinner, you lucky duck, you."
print(guests[0].title() + message)
print(guests[1].title() + message)

del(guests[0])
del(guests[0])
print(guests)
