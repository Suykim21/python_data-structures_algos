# Reverse linked list
# 1 -> 2 - > 3 => 3 -> 2 -> -1

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # Iterative
    def reverse(self):
        prev = None
        current = self.head
        # while current exists and its not null
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev




