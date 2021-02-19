class PyFileWalker:
    def __init__(self, path):
        self.path = path

    def __iter__(self):
        return self

    def __next__(self):
        # glogb, oswal
        return nextfile
        raise StopIteration

pywalker = PyFileWalker('.')
it = iter(pywalker)
next(pywalker) # test.py, test2.py, StopIteration