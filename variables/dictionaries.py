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


# 6.6 Rivers
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
