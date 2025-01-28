fruits = ["apple", "banana", "orange", "grape"]


# NOTE Not using typing. We will cover it on Day 06
def print_fruits(fruits):
    # Using AND operator
    # NOTE We will cover 'in' operator on Day 02
    if "apple" in fruits and "banana" in fruits:
        print("I have both apple and banana!")

    # Using OR operator
    if "orange" in fruits or "grape" in fruits:
        print("I have either orange or grape!")

    # Using IF statement
    if "apple" in fruits:
        print("I have an apple!")
    else:
        print("I don't have an apple!")

    # Using FOR loop
    for fruit in fruits:
        print("I have", fruit)

    # Applying all concepts twice
    # NOTE range() will be covered on Day 02
    for _ in range(2):
        if "apple" in fruits and "banana" in fruits:
            print("I have both apple and banana!")
        if "orange" in fruits or "grape" in fruits:
            print("I have either orange or grape!")
        if "apple" in fruits:
            print("I have an apple!")
        else:
            print("I don't have an apple!")
        for fruit in fruits:
            print("I have", fruit)


# NOTE We will cover __name__ == '__main__' on Day 06
if __name__ == "__main__":
    print_fruits(fruits)
