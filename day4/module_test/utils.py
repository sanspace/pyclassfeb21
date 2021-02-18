def say_hello(times=1):
    for _ in range(times):
        print("hello!")

def say_hi(name="there!"):
    print(f"hi {name}")


if __name__ == '__main__':
    say_hello(2)
    print(__name__)