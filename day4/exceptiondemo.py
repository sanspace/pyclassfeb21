# try:
#     guess = int(input("Enter a guess: "))
# except ValueError:
#     print("The Value you entered doesn't match our expectations")
# except KeyError:
#     print("The Keey does not exist")

def foo(x):
    return 1/x

def bar(x):
    try:
        print(foo(x))
    except ValueError:
        pass
    except TypeError:
        print("Watch your type!:", err)
    except ZeroDivisionError as err:
        print("Watch it! Can't divide by zero:", err)
    except:
        print("some error that we do not know")
    else:
        print("I'm here")
    finally:
        print("we're all done")

bar(0)

try:
    pass # always runs 1
except:
    pass # only on exception 0
else:
    pass # only when there's no excpetion
finally:
    pass # always runs 1