# Define a class to represent a node in a singly linked list
class Node:
    
    # Initialize the node with data and set the next pointer to None
    def __init__(self, data):
        self.data = data
        self.next = None

# Define a class to represent the singly linked list
class SinglyLinkedList:
    
    # Initialize the singly linked list with a head pointer set to None
    def __init__(self):
        self.head = None
    
    # Method to traverse the linked list and print the data of each node
    def traversal(self):
        # Check if the list is empty
        if self.head is None:
            print("Head is Empty ")
        else:
            # Start from the head node
            a = self.head
            # Traverse through the list until the end
            while a is not None:
                print(a.data, end="----->")
                # Move to the next node
                a = a.next

    # Method to insert a new node at the beginning of the linked list
    def insertion_at_beginning(self, data):
        print()
        # Create a new node with the given data
        nb = Node(data)
        # Set the next of the new node to the current head
        nb.next = self.head
        # Update the head to the new node
        self.head = nb
        
    # Method to insert a new node at the end of the linked list
    def insertion_at_end(self, data):
        print()
        # Create a new node with the given data
        ne = Node(data)
        # Start from the head node
        a = self.head
        # Traverse to the last node
        while a.next is not None:
            a = a.next
        # Set the next of the last node to the new node
        a.next = ne
    
    # Method to insert a new node at a specific position in the linked list
    def insertion_in_between(self, position, data):
        print()
        # Create a new node with the given data
        nbw = Node(data)
        # Start from the head node
        a = self.head
        # Traverse to the node just before the desired position
        for i in range(1, position - 1):
            a = a.next
        # Set the next of the new node to the next node in the list
        nbw.next = a.next
        # Set the next of the previous node to the new node
        a.next = nbw

    # Method to delete the node at the beginning of the linked list
    def deletion_at_beginning(self):
        print()
        # Get the current head node
        a = self.head
        # Update the head to the next node
        self.head = a.next
        # Set the next of the old head node to None
        a.next = None

    # Method to delete the node at the end of the linked list
    def deletion_at_end(self):
        print()
        # Start from the head node
        prev = self.head
        # Get the second node
        a = self.head.next
        # Traverse to the last node while keeping track of the previous node
        while a.next is not None:
            a = a.next
            prev = prev.next
        # Set the next of the second last node to None
        prev.next = None
    
    # Method to delete a node at a specific position in the linked list
    def deletion_in_between(self, position):
        print()
        # Start from the head node
        prev = self.head
        # Get the second node
        a = self.head.next
        # Traverse to the node just before the desired position
        for i in range(1, position - 1):
            a = a.next
            prev = prev.next
        # Set the next of the previous node to the next node of the node to be deleted
        prev.next = a.next
        # Set the next of the deleted node to None
        a.next = None

# Create nodes with data
n1 = Node(5)
n2 = Node(10)
n3 = Node(15)
n4 = Node(20)

# Create an instance of SinglyLinkedList and link the nodes
sll = SinglyLinkedList()
sll.head = n1
n1.next = n2
n2.next = n3
n3.next = n4

# Traverse and print the linked list
sll.traversal()

# Insert a new node with data '0' at the beginning
sll.insertion_at_beginning(0)
sll.traversal()

# Insert a new node with data '25' at the end
sll.insertion_at_end(25)
sll.traversal()

# Insert a new node with data '7.5' at the 3rd position
sll.insertion_in_between(3, 7.5)
sll.traversal()

# Delete the node at the beginning
sll.deletion_at_beginning()
sll.traversal()

# Delete the node at the end
sll.deletion_at_end()
sll.traversal()

# Delete the node at the 3rd position
sll.deletion_in_between(3)
sll.traversal()
