# Unlimited/unspec. number of inputs.
# * collects all the arguments in a tuple
def add(*args):
    print(args[4])

    sum = 0
    for n in args:
        sum += n
    return sum


print(add(5, 10, 9, 13, 1, 8, 2, 13, 11))


# Unlimited keyword arguments
def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(make="Bently", model="GTR")
print(my_car.model)