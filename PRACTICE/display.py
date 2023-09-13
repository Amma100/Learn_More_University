# display users name and age

try:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    new_value = int(input("Enter your value: "))

    # set condition
    if new_value == age:
        print("\nHello", name, ":)")
    else:
        print(":( wrong age")
except:
    print("Enter your age in digits...")
