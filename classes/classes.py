# 9.1: Restaurant 
class Restaurant():
    """ Defining a model of a restaurant """

    def __init__(self, name, type_of_cuise):
        """ Initialize name and type of cuisine of restaurant. """
        self.name = name
        self.type_of_cuise = type_of_cuise

    def describe_restaurant(self):
        """ Prints the two peices of information """
        print(self.name.title() + ' serves ' + self.type_of_cuise + '.')

    def open_restaurant(self):
        """ Prints that the restaurant is open. """
        print(self.name.title() + ' is open.')



dominos = Restaurant('Dominos', 'cheap pizza')
dominos.describe_restaurant()
dominos.open_restaurant()