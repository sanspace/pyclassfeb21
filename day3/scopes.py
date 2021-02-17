print("I'm a built-in") # built-in scope
name = "san" # global scope (of this current module)

def hello():
    dev = "John"
    def greeting():
        greeting = "hello" # local var (innermost)
        print(dev) # using from enclosed score

# innermost (greeting var) -> enclosed (dev) -> global (name) -> built-in (print, len)

