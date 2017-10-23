# Find Operation
# Big-O Notation: Time Complexity to Find/Search O(n); n == #items (depends on size of the list)

class Node(object):
    def __init__(self, data):
        self.next_node = None
        self.data = data

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def find(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next_node
        return False

    # Converting linked list to python list
    def to_list(self):
        l = []
        current_node = self.head
        while current_node:
            l.append(current_node.data)
            current_node = current_node.next_node
        return l
