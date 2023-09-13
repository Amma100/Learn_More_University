# a function to return the cube root of any number

def cube_root(new_num):
    value = new_num**(1/3)
    return value


# use try and except for values out of range
try:
    Number = float(input("Enter a number: "))
    a = "j"
    b = (-1 * Number)
    if Number == 0:
        print("\nThe cube root of {} is".format(Number), cube_root(Number))
    elif Number > 0:
        print("\nThe cube root of {} is".format(Number), cube_root(Number))
    else:
        print("\nThe cube root of", Number, "is (",a,"+",cube_root(b),")")
except:
    print("Please enter your number as digit...")
