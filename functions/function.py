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


# Magicians

magicians = ['Daid Blaine', 'Gandalf', 'Pete']

def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())

show_magicians(magicians)
