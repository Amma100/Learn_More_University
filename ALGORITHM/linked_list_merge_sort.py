from linked_list import Linkedlist


def merge_sort(linked_list):
    if Linkedlist.size() == 1:
        return linked_list
    elif Linkedlist.head is None:
        return linked_list

    left_half, right_half = split(linked_list)

    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(linked_list):
    if Linkedlist is None or Linkedlist.head is None:
        left_half = linked_list
        right_half = None
        return left_half, right_half
    else:
        size = Linkedlist.size()
        mid = size // 2

        mid_node = Linkedlist.node_at_index(mid - 1)

        left_half = linked_list
        right_half = Linkedlist()
        right_half.head = mid_node.next_node
        mid_node.next_node = None


        return left_half, right_half


def merge(left, right):
    merged = Linkedlist()
    merged.add(0)
    current = merged.head

    left_head = left.head
    right_head = right.head

    while left_head is not None or right_head is not None:
        if left_head is None:
            current.next_node = right_head
            right_head = right_head.next_node
        elif right_head is None:
            current.next_node = left_head
            left_head = left_head.next_node
        else:
            left_data = left_head.data
            right_data = right_head.data
            if left_data < right_data:
                current.next_node = left_head
                left_head = left_head.next_node
            else:
                current.next_node = right_head
                right_head = right_head.next_node
        current = current.next_node

    head = merged.head.next_node
    merged.head = head


l = Linkedlist()
l.add(10)
l.add(200)
l.add(50)
l.add(13)
l.add(45)
l.add(67)

print(l)
sorted_linked_list = merge_sort(l)
print(sorted_linked_list)
