# check if user number is positive or negative
try:
    num = float(input("Enter your number: "))
    if num < 0:
        print(num, "is negative :(")
    else:
        print(num, "is positive :)")
except:
    print("Error!!!\nEnter number in digit")
