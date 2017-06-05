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
