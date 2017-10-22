class Node(object):

    def __init__(self, value):

        self.value = value
        self.nextnode = None
        self.prevnode = None

a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.prevnode = a
b.nextnode = c
c.prevnode = b

# circular linked list
c.nextnode = a