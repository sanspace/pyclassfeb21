# l = [1, 2, 3]
# # get an iterable
# it = iter(l)
# # get next item from the iterable
# next(it)
# # until you stop iteration
# when you see StopIteration error

class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

rev = Reverse('python')
it = iter(rev)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

# for i in rev:
#     print(i)