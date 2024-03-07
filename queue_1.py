from node import Node



class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = None

    def enqueue(self, value):
        self.length =+ 1
        node = Node(value)

        if self.length == 1:
            self.head = node 
            return
        
        if not self.tail:
            self.tail = node
            self.head.right = node
            return
        
        old_tail = self.tail
        self.tail = node
        old_tail.right = node
        

    def deque(self):
        if not self.length:
            return
        
        old_head = self.head

        self.head = old_head.right
        self.length -= 1
        old_head.right = None

        return old_head

    def peek(self):
        return self.head.value

queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(4)
queue.enqueue(5)

print(queue.head.right.right, '\n')

print(queue.deque())
print(queue.deque())

print(queue.peek(), ' Peeking')

print(queue.deque())
print(queue.deque())
