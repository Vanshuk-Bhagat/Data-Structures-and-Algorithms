class Queue:
    def __init__(self):
        # Initialize the queue as an empty list
        self.queue = []

    def enqueue(self, item):
        # Add the item to the end of the queue
        self.queue.append(item)

    def dequeue(self):
        # Remove an item from the front of the queue if it's not empty
        if len(self.queue) < 1:
            print("Queue is empty")  # Print a message if the queue is empty
        else:
            self.queue.pop(0)  # Remove the first item from the queue

    def display(self):
        # Display the current elements in the queue
        print(self.queue)
            
# Create a new Queue object
q = Queue()

# Add elements to the queue
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)

# Display the current state of the queue
q.display()

# Remove an element from the front of the queue
q.dequeue()

# Display the state of the queue after dequeuing
q.display()
