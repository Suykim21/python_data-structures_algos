# Remove Operation
# Big-O Notation: Time Complexity to Remove/Delete O(1)

class Node(Object):
    def __init__(self, data):
        self.next_node = None
        self.data = data

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def remove(self, data):
        previous_node = None
        current_node = self.head
        # while current node exists
        while current_node:
            if current_node.data == data:
                # if previous node exists
                if previous_node:
                    # deleting node ex: 1(p) -> 2(c) -> 3(cn) => 1(p) -> 3(cn)
                    previous_node.next_node = current_node.next_node
                else:
                    # if its at first index, replace head ex: 1(hc) -> 2(cn) => 2(hc) 
                    self.head = current_node.next_node
                self.size -= 1
                return True
            previous_node = current_node
            current_node = current_node.next_node
        return False

    def remove_at(self, index):
        previous_node = None
        current_node = self.head
        i = 0

        while i < index and current_node.next_node:
            previous_node = current_node
            current_node = current_node.next_node
            i += 1

        if i == index:
            previous_node.next_node = current_node.next_node
            return True
        else:
            return False


