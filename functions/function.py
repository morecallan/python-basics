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
    print("You should make a shirt: ")
    print("\tSize: " + size)
    print("\tText: " + text_of_message)

make_tshirt('X-Small', 'Peace, bitch.')
make_tshirt(text_of_message='Peace, bitch.', size='X-Small')
