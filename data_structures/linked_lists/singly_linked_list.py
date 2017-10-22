class Node(object):

    def __init__(self, value):

        self.value = value
        self.nextnode = None

a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c

# prints 1
a.value

# prints 2
a.nextnode.value

