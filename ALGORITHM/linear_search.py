def linear_search(list, target):
    """
    Get all the index in the list
    """
    for i in range(0, len(lst)):
        if lst[i] == target:
            return i
    return None


def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")


lst = []

while True:
    try:
        numbers = input("Enter your number: ")
        new_num = float(numbers)
        if new_num == 0:
            break
        lst.append(new_num)
        lst.sort()
    except:
        print("You entered an invalid input")

print(lst)
result = linear_search(lst, 15)
verify(result)
