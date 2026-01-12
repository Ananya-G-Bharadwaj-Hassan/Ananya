
class Squares:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        
    def __iter__(self):
        for value in range(self.start, self.stop + 1):
            yield value ** 2
            
i = iter(Squares(1, 3))
print(next(i))
print(next(i))
print("Vismaya")
print("Pavan")
print("Keerthana")
print(next(i))

class CallExample:
    def __init__(self, val):
        self.val = val
        
    def mul(self, b):
        return self.val * b

myobj = CallExample(5)

myobj.mul(10)