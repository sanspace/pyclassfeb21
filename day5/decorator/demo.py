from functools import wraps


def say_hi(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("start")
        func(*args, **kwargs)
        print("end")
    return wrapper

@say_hi
def announce(name):
    print(f'breakfast ready! {name}')

@say_hi
def bedtime():
    print('time for bed')

@say_hi
def greet(name="san", time="morning"):
    print(f"{name} {time}")

# announce = outer(announce)
announce("san")

# bedtime = outer(bedtime)
bedtime()

greet("john", "evening")


