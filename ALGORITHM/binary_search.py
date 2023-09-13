def binary_search(lst, target):
    first = 0
    last = len(lst) - 1

    while first <= last:
        midpoint = (first + last) // 2

        if lst[midpoint] == target:
            return midpoint
        elif lst[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None


def verify(index):
    if index is not None:
        print("Target found at index ", index)
    else:
        print("Target not found in list")


lst = []

while True:
    numbers = input("Enter your number: ")
    try:
        new_num = float(numbers)
        if new_num == 0:
            break
        lst.append(new_num)
        lst.sort()

    except:
        print("Invalid input")

print(lst)
result = binary_search(lst, 6)
verify(result)
