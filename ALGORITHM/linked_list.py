class Node:
    data = None
    next_node = None

    def __init__(self, mydata):
        self.data = mydata

    def __repr__(self):
        return "<Node data: %s>" % self.data


class Linkedlist:
    head = None

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def size(self):
        current = self.head
        count = 0

        while current is not None:
            count += 1
            current = current.next_node

        return count

    def add(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        current = self.head

        while current is not None:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def insert(self, data, index):
        if index == 0:
            self.add(data)
        if index > 0:
            new = Node(data)
            position = index
            current = self.head

            while position > 1:
                current = Node.next_node
                position -= 1

            previous = current
            new_next = current.next_node

            previous.next_node = new
            new.next_node = new_next

    def remove(self, key):
        current = self.head
        previous = None
        found = False

        while current is not None and not found:
            if current.data is key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data is key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
        return current

    def node_at_index(self, index):
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0

            while position < index:
                current = current.next_node
                position += 1
            return current

    def __repr__(self):
        nodes = []
        current = self.head

        while current is not None:
            if current is self.head:
                nodes.append("[Home: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node
        return "--> ".join(nodes)
