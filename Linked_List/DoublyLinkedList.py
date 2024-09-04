# Node class represents a node in a doubly linked list
class Node:
    def __init__(self, data):
        # Initialize the node with data, and set next and prev pointers to None
        self.data = data
        self.next = None
        self.prev = None

# Doubly Linked List class to manage the list operations
class doubly_linked_list:
    def __init__(self):
        # Initialize the list with the head pointer set to None (empty list)
        self.head = None

    # Function to traverse the list in forward direction
    def forward_traversal(self):
        if self.head is None:
            print("There is no data in the list")
        else:
            # Start from the head and move forward
            a = self.head
            while a is not None:
                # Print the data in the current node
                print(a.data, end=" ---->")
                # Move to the next node
                a = a.next
            print()  # For a new line after the traversal

    # Function to traverse the list in backward direction
    def backward_traversal(self):
        print()  # For a new line before the traversal
        if self.head is None:
            print("There is no data in the list")
        else:
            # Move to the last node of the list
            a = self.head
            while a.next is not None:
                a = a.next
            # Traverse backward using the prev pointer
            while a is not None:
                # Print the data in the current node
                print(a.data, end="<-----")
                # Move to the previous node
                a = a.prev
            print()  # For a new line after the traversal

    # Function to insert a node at the beginning of the list
    def insertion_beginning(self, data):
        print()  # For a new line before insertion
        # Create a new node
        nb = Node(data)
        if self.head is None:
            # If the list is empty, set the new node as head
            self.head = nb
        else:
            # If the list is not empty, adjust the pointers
            self.head.prev = nb
            nb.next = self.head
            self.head = nb  # Set the new node as the head

    # Function to insert a node at the end of the list
    def insertion_end(self, data):
        print()  # For a new line before insertion
        # Create a new node
        ne = Node(data)
        if self.head is None:
            # If the list is empty, set the new node as head
            self.head = ne
        else:
            # If the list is not empty, traverse to the last node
            a = self.head
            while a.next is not None:
                a = a.next
            # Adjust the pointers to insert the new node at the end
            a.next = ne
            ne.prev = a

    # Function to insert a node at a specific position in the list
    def insertion_between(self, position, data):
        print()  # For a new line before insertion
        if position <= 1:
            print("Invalid position")
            return
        # Create a new node
        nbw = Node(data)
        a = self.head
        # Traverse to the node before the desired position
        for i in range(1, position - 1):
            if a is None:
                print("Position out of range")
                return
            a = a.next
        # If the position is out of range, print an error message
        if a is None or a.next is None:
            print("Position out of range")
            return
        # Adjust the pointers to insert the new node
        nbw.prev = a
        nbw.next = a.next
        a.next.prev = nbw
        a.next = nbw

    # Function to delete the node at the beginning of the list
    def deletion_at_beginning(self):
        print()  # For a new line before deletion
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            # If the list has only one node, set head to None
            self.head = None
        else:
            # Move the head to the next node and adjust pointers
            self.head = self.head.next
            self.head.prev = None

    # Function to delete the node at the end of the list
    def deletion_at_end(self):
        print()  # For a new line before deletion
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            # If the list has only one node, set head to None
            self.head = None
        else:
            # Traverse to the last node
            a = self.head
            while a.next is not None:
                a = a.next
            # Adjust the pointers to remove the last node
            a.prev.next = None

    # Function to delete a node at a specific position in the list
    def deletion_between(self, position):
        print()  # For a new line before deletion
        if self.head is None:
            print("List is empty")
            return
        a = self.head
        # Traverse to the node at the desired position
        for i in range(1, position):
            if a is None or a.next is None:
                print("Position out of range")
                return
            a = a.next
        # Adjust the pointers to remove the node from the list
        a.prev.next = a.next
        if a.next is not None:
            a.next.prev = a.prev

# Example usage of the doubly linked list

# Create the initial nodes and link them
n1 = Node(5)
dll = doubly_linked_list()
dll.head = n1
n2 = Node(10)
n2.prev = n1
n1.next = n2
n3 = Node(15)
n3.prev = n2
n2.next = n3
n4 = Node(20)
n4.prev = n3
n3.next = n4

# Perform various operations on the list
dll.forward_traversal()         # Output the list in forward direction
dll.backward_traversal()        # Output the list in backward direction
dll.insertion_beginning(0)      # Insert 0 at the beginning
dll.forward_traversal()         # Output the list again in forward direction
dll.backward_traversal()        # Output the list again in backward direction
dll.insertion_end(25)           # Insert 25 at the end
dll.forward_traversal()         # Output the list again in forward direction
dll.backward_traversal()        # Output the list again in backward direction
dll.insertion_between(3, 7.5)   # Insert 7.5 at position 3
dll.forward_traversal()         # Output the list again in forward direction
dll.backward_traversal()        # Output the list again in backward direction
dll.deletion_at_beginning()     # Delete the node at the beginning
dll.forward_traversal()         # Output the list again in forward direction
dll.backward_traversal()        # Output the list again in backward direction
dll.deletion_at_end()           # Delete the node at the end
dll.forward_traversal()         # Output the list again in forward direction
dll.backward_traversal()        # Output the list again in backward direction
dll.deletion_between(3)         # Delete the node at position 3
dll.forward_traversal()         # Output the list again in forward direction
dll.backward_traversal()        # Output the list again in backward direction
