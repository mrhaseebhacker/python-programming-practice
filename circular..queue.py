class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size  # Fixed size list
        self.front = -1
        self.rear = -1

    def enqueue(self, value):
        # Check if queue is full (circular condition)
        if (self.rear + 1) % self.size == self.front:
            print("Queue Overflow! Cannot insert", value)
            return

        # First element being inserted
        if self.front == -1:
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = value
        else:
            # Move rear to next circular position
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = value

        print(f"Enqueued: {value}")

    def dequeue(self):
        # Check if queue is empty
        if self.front == -1:
            print("Queue Underflow! Nothing to dequeue.")
            return

        removed = self.queue[self.front]
        # Only one element left
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            # Move front to next circular position
            self.front = (self.front + 1) % self.size

        print(f"Dequeued: {removed}")
        return removed

    def display(self):
        if self.front == -1:
            print("Queue is empty.")
            return

        print("Queue contents:", end=" ")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()

cq = CircularQueue(5)

cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)  # This should trigger overflow

cq.display()

cq.dequeue()
cq.dequeue()

cq.display()

cq.enqueue(60)
cq.enqueue(70)  # This should now work due to free space

cq.display()
