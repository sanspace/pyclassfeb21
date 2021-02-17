# Stack is a Data structure
# that follows LIFO (Last In First Out)

stack = [] # empty list

def push(el):
    stack.append(el)
    print("pushed ", el)

def pop():
    return stack.pop()

def length():
    return len(stack)

def show():
    print(stack)

def is_empty():
    return len(stack) == 0

# try out
show()
print(is_empty())
push(1)
push(2)
show()
pop()
show()
print(is_empty())
pop()
print(is_empty())
show()
