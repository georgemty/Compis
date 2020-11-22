import sys
class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []

    def size(self):
        return len(self.stack)

    def push(self, data):
        self.stack.append(data)

    def pop(self):
         if self.size() > 0:
             return self.stack.pop()
         print('Pila vacia....')

    def peek(self):
        return self.stack[len(self.stack)-1]
