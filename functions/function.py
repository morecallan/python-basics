# 8.1 Message

def display_message():
    """ Displays message to user about user."""
    print('I\'m learnin\' \'bout functions.')

display_message()


# 8.2 Favorite Book
def favorite_book(title):
    """Displays user's favorite book give the book's title."""
    print('My favorite book is ' + title.title() + '.')

favorite_book("alice in wonderland")


# 8.3 T-Shirt

def make_tshirt(size, text_of_message):
    """ Prints the size of the T-shirt and the message to print on it. """
    print("You should make a shirt: ")
    print("\tSize: " + size)
    print("\tText: " + text_of_message)

make_tshirt('X-Small', 'Peace, bitch.')
make_tshirt(text_of_message='Peace, bitch.', size='X-Small')


# 8.4 Large Shirts

def make_large_tshirt(size="XL", text_of_message="I Love Python"):
    """ Prints the size of the T-shirt and the message to print on it."""
    print("You should make a shirt: ")
    print("\tSize: " + size)
    print("\tText: " + text_of_message)

make_large_tshirt()
make_large_tshirt(size='Medium')
make_large_tshirt(size='Small', text_of_message="Yo")


# 8.5 Cities

def describe_cities(city_name, country_name="the United States"):
    """ Prints a city and country name, neatly formatted """
    print(city_name.title() + " is in " + country_name + ".")

describe_cities("Nashville")
describe_cities("Richmond")
describe_cities("Paris", country_name="France")


# 8.6 City Names

def city_country(city_name, country_name):
    """ Returns a city and country name, neatly formatted """
    return city_name.title() + ', ' + country_name.title()

paris = city_country("paris", "france")
print(paris)


# 8.7 Albums

def make_album(artist_name, album_title, num_of_tracks = ''):
    """ Returns a dictionary representation of album information. """
    album = {'artist_name': artist_name, 'album_name': album_title}

    if (num_of_tracks):
        album['number_of_tracks'] = num_of_tracks

    return album

album_thriller = make_album('Michael Jackson', 'Thriller')
album_back_in_black = make_album('AC/DC', 'Back in Black')
album_dark_side_of_the_moon = make_album('Pink Floyd', 'Dark Side of the Moon', 10)

print(album_thriller)
print(album_back_in_black)
print(album_dark_side_of_the_moon)

# 8.8 User Album

def make_album(artist_name, album_title, num_of_tracks = ''):
    """ Returns a dictionary representation of album information. """
    album = {'artist_name': artist_name, 'album_name': album_title}

    if (num_of_tracks):
        album['number_of_tracks'] = num_of_tracks

    return album

def check_for_quit(value):
    if (value == 'q'):
        return True

# This while loop checks for the q input at each input prompt to see if the user wants to exit the program.
while True:
    print("Enter album information and get a dictionary back, enter 'q' at any point to quit: ")

    artist_name = input("Enter an artist name: ")
    if (check_for_quit(artist_name)):
        break

    album_name = input("Enter an album name: ")
    if (check_for_quit(album_name)):
        break

    num_of_tracks = input("Enter a number of tracks: ")
    if (check_for_quit(num_of_tracks)):
        break

    make_album(artist_name, album_name, num_of_tracks)


# 8.9 Magicians

magicians = ['Daid Blaine', 'Gandalf', 'Pete']

def show_magicians(magicians):
    """ Receives a list of magicians and prints them one at a time. """
    for magician in magicians:
        print(magician.title())

show_magicians(magicians)

# 8.10 Great magicians

great_magicians = []

def make_great(magical_beings_list, new_magicial_beings_list):
    while magical_beings_list:
        """ Takes a list of magicians, removes them from the original list, manipulates to values then adds them to the new list.  """
        bye_magician = magical_beings_list.pop()
        new_magicial_beings_list.append(bye_magician.title() + " the Great")

def print_magicians(magician_list):
    """ Prints a list of magicians """
    for magician in magician_list:
        print(magician)


make_great(magicians, great_magicians)
print_magicians(great_magicians)

# 8.10 Attempt 2, not using multiple lists, because that seems silly.

magicians = ['Frederick', 'Mark', 'Alana']

def add_great(magician_list):
    """ Takes a list of magicians and manipulates each item in the list to add 'the Great' to their title. """
    for i in range(len(magician_list)):
        magician_list[i] = magician_list[i] + ' the Great!'

def print_magicians(magician_list):
    """ Prints a list of magicians """
    for magician in magician_list:
        print(magician)

add_great(magicians)
print_magicians(magicians)


# 8.11 Magicians without manipulation
# In order for this to work, 8.10 attempt 2 needs to be commented out and 8.10 og function calls need to be commented out

make_great(magicians[:], great_magicians)
print_magicians(magicians)
print_magicians(great_magicians)
