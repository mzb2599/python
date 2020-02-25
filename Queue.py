class queue:
    def __init__(self, max_size, size=0, front=0, rear=0):
        self.queue = [[] for i in range(5)]
        self.max_size = max_size
        self.size = size
        self.front = front
        self.rear = rear
    def enqueue(self, data):
        if not self.isFull():
            self.queue[self.rear] = data
            self.rear = int((self.rear + 1) % self.max_size)
            self.size += 1
        else:
            print("Queue is full")
    def dequeue(self):
        if not self.isFull():
            print(self.queue[self.front], 'is removed')
            self.front = int((self.front + 1) % self.max_size)
            self.size -= 1
        else:
            print('Queue is Empty')
    def isEmpty(self):
        return self.size == 0
    def isFull(self):
        return self.size == self.max_size
    def show(self):
        print('Queue contents are :')
        for i in range(self.size):
            print(self.queue[i])

O = 0
q=queue(5)
while (O != 4):
    print('1-Enqueue\n2-Dequeue\n3-Display Queue\n4-Exit')
    O = int(input("Enter the operation : "))
    if O == 1:
        n = int(input('Enter the element to enqueue: '))
        q.enqueue(n)
    elif O == 2:
         q.dequeue()
    elif O == 3:
        q.show()

        
# '''  
# C:\Users\MOHD ZAKI\Desktop\Sem4\python\college>py Queue.py
# 1-Enqueue
# 2-Dequeue
# 3-Display Queue
# 4-Exit
# Enter the operation : 1
# Enter the element to enqueue: 5
# 1-Enqueue
# 2-Dequeue
# 3-Display Queue
# 4-Exit
# Enter the operation : 1
# Enter the element to enqueue: 1
# 1-Enqueue
# 2-Dequeue
# 3-Display Queue
# 4-Exit
# Enter the operation : 1
# Enter the element to enqueue: 6
# 1-Enqueue
# 2-Dequeue
# 3-Display Queue
# 4-Exit
# Enter the operation : 3
# Queue contents are :
# 5
# 1
# 6
# 1-Enqueue
# 2-Dequeue
# 3-Display Queue
# 4-Exit
# Enter the operation : 2
# Enter the element to dequeue: 1
# 5 is removed
# 1-Enqueue
# 2-Dequeue
# 3-Display Queue
# 4-Exit
# Enter the operation : 3
# Queue contents are :
# 5
# 1
# 1-Enqueue
# 2-Dequeue
# 3-Display Queue
# 4-Exit
# Enter the operation : 4
# '''
