class Stack:
    """A well-known data structure…"""

    def __init__(self):        # constructor
        self.items = []

    def push(self, x):
        self.items.append(x)    # the sky is the limit

    def pop(self):
        x = self.items[-1]        # what happens if it’s empty?
        del self.items[-1]
        return x

    def empty(self):
        return len(self.items) == 0    # Boolean result

dev_stack = Stack()
print(dev_stack.empty())
dev_stack.push('Guido')
dev_stack.push('Raymond')
print(dev_stack.items)
print(dev_stack.pop())
print(dev_stack.items)
print(dev_stack.pop())
print(dev_stack.items)
print(dev_stack.empty())

lang_stack = Stack()
lang_stack.push('python')
lang_stack.push('golang')
print(lang_stack.items)

print(dev_stack.items)