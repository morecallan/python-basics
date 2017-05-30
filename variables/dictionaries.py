# 6.1 Person:
megen = {'first_name': 'Megen', 'last_name': 'Mitchell', 'age': 26, 'city': 'Boone, NC'}
print("Her name is " + megen['first_name'].title() + " " + megen['last_name'].title() + ". She is " + str(megen['age']) + " years old and lives in " + megen['city'] + ".")


# 6.2 Favorite Numbers
fav_nums = {
    'megen': 291,
    'sarah': 3,
    'heather': 18,
    'marissa': 21,
    'leigh': 99
}

print('Megen\'s favorite number is: ' + str(fav_nums['megen']))
print('Sarah\'s favorite number is: ' + str(fav_nums['sarah']))
print('Heather\'s favorite number is: ' + str(fav_nums['heather']))
print('Marissa\'s favorite number is: ' + str(fav_nums['marissa']))
print('Leigh\'s favorite number is: ' + str(fav_nums['leigh']))


# 6.4 Favorite Numbers 2
for k, v in sorted(fav_nums.items()):
    print(k.title() + '\'s favorite number is: ' + str(v))


# 6.5 Rivers
rivers = {
    'nile': 'egypt',
    'james': 'united states',
    'yangtze': 'china'
}

for river, country in rivers.items():
    print("The " + river.title() + " runs through " + country.title() + ".")

print("This is just a list of all the rivers:  ")
for river in sorted(rivers):
    print(river.title())

print("This is just a list of all the countries:  ")
for country in sorted(rivers.values()):
    print(country.title())


# 6.6 Polling
fav_languages = {
'jen': 'python',
'sarah': 'node',
'edward': 'c#',
'phil': 'python'
}

to_take_poll = ['phil', 'margot', 'mister t', 'sarah']

for person in sorted(to_take_poll):
    if person.lower() not in fav_languages.keys():
        print(person.title() + ", please take our poll!")
    else:
        print(person.title() + ", thank you for taking our poll!")


# 6.7 People (referencing megen from 6.1)
sarah = {'first_name': 'Sarah', 'last_name': 'Demind', 'age': 27, 'city': 'Nashville, TN'}
heather = {'first_name': 'Heaher', 'last_name': 'Sharpe', 'age': 26, 'city': 'Raleigh, NC'}

people = [megen, sarah, heather]

for person in people:
    full_name = person['first_name'].title() + ' ' + person['last_name'].title()
    print('My friend, ' + full_name + ' is ' + str(person['age']) + ' years old and lives in ' + person['city'] + '.')


# 6.8 Pets
seymour = {'name': 'seymour', 'type': 'dog', 'owner': 'callan'}
frontier = {'name': 'frontier', 'type': 'dog', 'owner': 'lilian'}
pete = {'name': 'pete', 'type': 'goat', 'owner': 'megen'}
mango = {'name': 'mango', 'type': 'fish', 'owner': 'nick'}

pets = [seymour, frontier, pete, mango]

for pet in pets:
    print(pet['name'].title() + ' is a ' + pet['type'] + ' and is owned by ' + pet['owner'].title() + '.')


# 6.9 Favorite Places
fav_places = {
    'megen': ['Alaska', 'the woods', 'ashville, NC'],
    'sarah': ['Paris', 'Charlotte, NC', 'Nashville, TN'],
    'marissa': ['bed']
}

for person, places in fav_places.items():
    if len(places) > 1:
        print(person.title() + '\'s favorite places are: ')
        for place in places:
            print('\t' + place)
    else:
        print(person.title() + '\'s favorite place is ' + places[0] + '.')


# 6.10 Favorite Numbers
fav_nums = {
    'megen': 291,
    'sarah': 3,
    'heather': 18,
    'marissa': 21,
    'leigh': 99
}

fav_nums['megen'] = [3, 6, 9, 44, 291]
fav_nums['sarah'] = [9, 3, 4]
fav_nums['heather'] = [77, 18]
fav_nums['marissa'] = [21, 69, 0]
fav_nums['leigh'] = [99]

for person, nums in fav_nums.items():
    if (len(nums) > 1):
        print(person.title() + '\'s favorite numbers are: ')
        for num in nums:
            print('\t' + str(num))
    else:
        print(person.title() + '\'s favorite numbers is: ' + str(nums[0]))
