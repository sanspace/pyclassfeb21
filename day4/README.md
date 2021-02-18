# Day 4

## Topics

  - packages
  - virtual environments and packages
  - exceptions
    - except
    - finally
    - else
    - raise
    - custom exceptions
  - i/0
    - string formatting
    - file handling
  - Iterators

## Refer

  - https://docs.python-guide.org/dev/virtualenvs/
  - https://rszalski.github.io/magicmethods/
  - https://docs.python.org/3/library/exceptions.html#built-in-exceptions

## Practice

  - Write an iterator yourself
    - Create a class that implements `__iter__` and `__next__` methods.
    - It should accept a string and provide an iterator that traverses every other character in the string i.e. given `hello`, provide `h`, `l`, `o` and `StopIteration` on consecutive next calls. Should work like below:
    ```python
      >>> j = Jumper('hello')
      >>> it = iter(j)
      >>> next(it)
      'h'
      >>> next(it)
      'l'
      >>> next(it)
      'o'
      >>> next(it)
      Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        File "<stdin>", line 9, in __next__
      StopIteration
      >>> j = Jumper('python')
      >>> it = iter(j)
      >>> next(it)
      'p'
      >>> next(it)
      't'
      >>> next(it)
      'o'
      >>> next(it)
      Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        File "<stdin>", line 9, in __next__
      StopIteration
      >>> exit()
    ```
  - create a CSV file containing names and experience of the participants. Note: Not xls, just a comma separated plain text file.
  - write a program to traverse the current directory (recursively) and print only python file names.
  - use standard lib sys to list all the command line args given to your program
  - Rewrite the guessing game program to throw a custom error when the user is out of tries. 
  - accept input from a user and handle type, value errors
  - demonstrate key and index errors in an example

## Extra Mile

  - use [requests](https://pypi.org/project/requests/) to grab contents of a web page and print the page title
    - create a virtual environment, install requests, access a website and print the title, add a requirements.txt with your environment packages (pip freeze) and share this repo
  - Can you create an iterator for the recursive directory traversal program above?
    - accept a path as input and provide an object that's an iterable the provides the python files available in that path (and in subdirs) one by one and at the end `StopIteration`
