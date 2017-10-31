# Add operation
# Big-O Notation: Time Complexity to Add/Insert O(1)

class Node(object):
    def __init__(self, data):
        self.next_node = None
        self.data = data

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, data):
        new_node = Node(data)
        # if self.tail or list exists
        if self.tail:
            self.tail.next_node = new_node
            self.tail = new_node
        # if list is empty
        else:
            self.head = new_node
            self.tail = new_node
        self.size += 1


    def add_at(self, data, index):
        new_node = Node(data)
        previous_node = None
        current_node = self.head
        i = 0
        # keep iterating until current node has next node.
        while i < index and current_node.next_node:
            previous_node = current_node
            current_node = current_node.next_node
            i += 1
        # Either we've reached the end of the list early or i is equal to our target index
        if i == index:
            previous_node.next_node = new_node
            new_node.next_node = current_node
            return True
        else:
            # List not long enough
            return False
