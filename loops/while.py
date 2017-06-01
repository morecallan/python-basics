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
