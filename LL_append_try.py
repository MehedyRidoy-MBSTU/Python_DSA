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

    # Print method to display the linked list
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end=" -> ")
            temp = temp.next
        print("None")

    # Append method to add a new node at the end of the linked list
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
###########################################

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.print_list()  # Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None

