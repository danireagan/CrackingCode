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
    
class sortedStack:
    def __init__(self):
        self.stack = Stack()
        self.tempStack = Stack()
    
    def push(self, val):
        if self.stack.top != None:
            if val > self.stack.top.data:
                while self.stack.top != None and val > self.stack.top.data:
                    self.tempStack.push(self.stack.pop())
                    
        self.stack.push(val)
        while self.tempStack.top != None:
            self.stack.push(self.tempStack.pop())

    def pop(self):
        if self.stack.top == None:
            print("Stack Empty")
            return -1
        val = self.stack.pop()
        return val
    
    def display(self):
        self.stack.display()

length = int(input("Enter the number of elements in stack"))
stack = sortedStack()
for i in range(length):
    stack.push(int(input(f"Enter the value {i}")))

stack.display()
