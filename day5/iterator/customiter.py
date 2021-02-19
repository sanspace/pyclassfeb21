class Jumper():

    def __init__(self, data):
        self.data = data
        self.index = 0
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.index > len(self.data) - 1:
            raise StopIteration
        item = self.data[self.index]
        self.index += 2
        return item

j = Jumper('hi') # __init__ will be called
it = iter(j) # __iter___ will be called
next(it) # __next__ will be called


