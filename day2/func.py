def say_hello(**kwargs):
    """says hello to any number of kwargs
    
    accepts any number of kwargs and
    loops over them....
    
    """

    print(kwargs)
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f"{key} = {value}")


print("first call")
say_hello()
print("second call")
say_hello(name="San")
print("third call")
say_hello(name="San", lang="Python", country="France", leader="Gandhi")

def add(num1, num2):
    return num1 + num2

print(add(2,3))

# positional args
# keyword args - more readable
# default args
# arbitrary args
# default returns None