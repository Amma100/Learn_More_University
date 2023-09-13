def split(lst):
    mid_point = len(lst) // 2
    left = lst[:mid_point]
    right = lst[mid_point:]

    return left, right


def merge(left, right):
    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1

    return l


def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    left_half, right_half = split(lst)

    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def verify_sorted(lst):
    n = len(lst)

    if n == 0 or n == 1:
        return True

    return lst[0] < lst[1] and verify_sorted(lst[1:])


new_list = [46, 53, 78, 16, 37, 55, 94, 5, 43, 0]

result = merge_sort(new_list)

print("\nResult: ", new_list)
print(verify_sorted(new_list))
print("\nResult: ", result)
print(verify_sorted(result))
