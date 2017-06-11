# 7.4 Pizza Toppings

prompt = "\nEnter a topping you want on your pizza."
prompt += "\n(Type 'quit' when you are done.): "

toppings = []

while True:
    topping = input(prompt)

    if topping.lower() == 'quit':
        break
    else:
        print("I'm adding " + topping.title() + " to your pizza!")
        toppings.append(topping)

print("Your pizza has the following toppings: ")
for toppin in toppings:
    print(toppin.title())


# 7.5 Movie Tickets

prompt = "\nEnter your age to receive your movie ticket price."
prompt += "\n(Type 'quit' when you are done.): "

response = "Your ticket price is: "

while True:
    age = input(prompt)

    if age == 'quit':
        break
    elif int(age) < 3:
        print(response + "free.")
    elif int(age) < 12:
        print(response + "$10.")
    else:
        print(respone + "$15.")


# 7.8 Deli

sandwich_orders = ['meatball sub', 'grilled cheese', 'pb&j', 'knuckle']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print("Making your " + current_sandwich + ".")
    finished_sandwiches.append(current_sandwich)

print("The following sandwiches have been made: ")
for sandwich in finished_sandwiches:
    print(sandwich)


# 7 BONUS Needle in the Haystack
current_val = 0

haystack = ["needle", "frog", "cat", "needle", "mint", "creep", "needle"]
needle_collection = []

while "needle" in haystack:
     current = haystack[current_val]

     if (current == "needle"):
         print("found a needle! removing it!")
         haystack.remove("needle")
         needle_collection.append(current)

     current_val = current_val + 1

print(haystack)
print(needle_collection)

# 7.9 No Pastrami

sandwich_orders = ['meatball sub', 'pastrami', 'grilled cheese', 'pastrami', 'pb&j', 'knuckle', 'pastrami']
finished_sandwiches = []

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)
