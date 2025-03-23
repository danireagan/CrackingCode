class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
    
class Stack:
    def __init__(self):
        self.top = None
        
    def push(self, val):
        node = Node(val)
        node.next = self.top
        self.top = node
    
    def pop(self):
        if self.top == None:
            print("Stack Empty")
            return -1
        val = self.top.data
        self.top = self.top.next
        return val
    
    def display(self):
        temp = self.top
        while temp != None:
            print(temp.data, end="->")
            temp=temp.next
    def peek(self):
        return self.top.data
    
class MyQueue:
    def __init__(self):
        self.stack = Stack()
        self.ReverseStack = Stack()
        self.active = 0

    def enqueue(self, val):
        if self.active != 0:
            while self.ReverseStack.top != None:
                self.stack.push(self.ReverseStack.pop())
            self.active = 0
        self.stack.push(val)

    def dequeue(self):
        if self.stack.top == None and self.ReverseStack.top == None:
            print("Queue is empty.")
            return -1
        if self.active != 1:
            while self.stack.top !=None:
                self.ReverseStack.push(self.stack.pop())
            self.active = 1
        return self.ReverseStack.pop()
    
    def display(self):
        if self.active == 0:
            print("The reverse queue is")
            self.stack.display()
            print("")
        else:
            print("The queue is ")
            self.ReverseStack.display()
            print("")


que = MyQueue()
size = int(input("Enter the number of values to enqueue"))
for i in range(size):
    que.enqueue(int(input(f"Enter value to enque {i}")))

que.display()
que.dequeue()
que.display()
que.dequeue()
que.display()
que.enqueue(34)
que.display()
que.dequeue()
que.display()