class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

####################################################

my_linked_list = LinkedList(4)
print(my_linked_list.head.value)  # Output: 4
print(my_linked_list.tail.value)  # Output: 4
print(my_linked_list.length)  # Output: 1
print(my_linked_list.head.next)  # Output: None
print(my_linked_list.tail.next)  # Output: None
print(my_linked_list.head.next)  # Output: None 