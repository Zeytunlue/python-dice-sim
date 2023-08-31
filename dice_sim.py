import random
while True:
    print("1. Roll the dice  2. To exit")
    choice = int(input("What do you want to do?: \n"))
    if choice == 1:
        number = random.randint(1, 6)
        print(number)
    if choice != 1:
        print("Goodbye!")
        break