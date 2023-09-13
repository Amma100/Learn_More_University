def recursive_binary_search(lst, target):
    if len(lst) == 0:
        return False
    else:
        lst.sort()
        midpoint = len(lst) // 2

        if lst[midpoint] == target:
            return True
        else:
            if lst[midpoint] < target:
                return recursive_binary_search(lst[midpoint + 1:], target)
            else:
                return recursive_binary_search(lst[:midpoint], target)


def verify(value):
    print("Target found: ", value)


numbers = [1, 12, 3, 14, 5, 6, 76, 28, 39, 10]
result = recursive_binary_search(numbers, 3)
verify(result)
