
# Defining the class, which will create nodes for our linked list
class Node:                         
    def __init__ (self, data):      # Node's constructor         
        self.data = data            
        self.next = None            

# Defining the class which will be our linked list and also defining the methods which will be used in our linked list                                        
class LinkedList:               
    def __init__ (self):            # Linked List's constructor
        self.head = None

# Defining a method which will print the whole linked list
    def printList (self):
        temp = self.head
        while (temp):
            print (temp.data)
            temp = temp.next

# Defining a method which will insert a new node at the beginning of the linked list
    def push (self, new_data):          
        new_node = Node(new_data)
        new_node.next = self.head       
        self.head = new_node

# Defining a method which will insert a new node after specified node
    def insertAfter (self, prev_node, new_data):
        if prev_node is None:
            print ("The given previous node must be in linked list.")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

# Defining a method which will insert a new node at the end of the linked list
    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

# Defining a method which will delete the first occurence of the node which matches the key
    def deleteNode(self, key):
        temp = self.head
        if temp is not None and temp.data == key:
            self.head = temp.next
            temp = None
            return
        while temp:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        prev.next = temp.next

# Defining a method which will reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
        

# The main logic starts from here
if __name__ == '__main__':

    mylist = LinkedList()                # Creating a new linked list

    mylist.head = Node(20)               # Creating new nodes and assigning data to them
    second = Node(50)
    third = Node(60)

    mylist.head.next = second            # Assigning pointers to the next node in the linked list
    second.next = third

    mylist.printList()                   # Printing the linked list
    
    mylist.push(10)                      # Creating a new node in the beginning
    mylist.printList()                   # Printing the linked list
    
    mylist.insertAfter(second, 15)       # Creating a new node after the node named second
    mylist.printList()                   # Printing the linked list

    mylist.append(100)                   # Creating a new node at the end of the linked list
    mylist.printList()                   # Printing the linked list

    mylist.deleteNode(60)                # Deleting the node which have the data 60
    mylist.printList()                   # Printing the linked list

    mylist.reverse()                     # Reversing the linked list
    mylist.printList()                   # Printing the linked list

# courtesy from Mad Programmer - Youtube channel.