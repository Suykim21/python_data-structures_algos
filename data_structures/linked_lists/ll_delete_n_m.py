# Delete N nodes after M nodes of a linked list
# Given a linked list and two integers M and N. Traverse the linked list such that you retain M nodes then delete next N nodes, continue the same till end of the linked list

# Input:
# M = 3, N = 2
# Linked List: 1->2->3->4->5->6->7->8->9->10
# Output:
# Linked List: 1->2->3->6->7->8

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):

    # Function to initailize head and tail
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # Function to insert a new node at the beginning
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to print the LinkedList
    def printList(self):
        temp = self.head
        while temp:
            print (temp.data)
            temp = temp.next

    def skipMdeleteN(self, M, N):
        current = self.head

        # The main loop that traverses through the whole list
        while current:
            # Skip M nodes
            for count in range(1, M):
                if current is None:
                    return
                current = current.next

            if current is None:
                return

            # Start from next node and delete N nodes
            t = current.next
            for count in range(1, N+1):
                if t is None:
                    break
                t = t.next
            
            # Link the previous list with remaining nodes
            current.next = t
            # Set Current pointer for next iteration
            current = t

    