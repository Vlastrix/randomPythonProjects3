# Put unlimited values using *args


def add(*args, result=0):
    for arg in args:
        result += arg
    return result


print(add(3, 3, 5))

# You can put default values for a function


def something(a=1, b=2, c=3):
    print(a)
    print(b)
    print(c)


something(2)

print("###############################################################################################")


def calc(n, **kwargs):
    # print(kwargs)
    # for key, value in kwargs.items():
    #     print(value)
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calc(n=2, add=3, multiply=5)


# .get returns None if dosen't find the key while using square brackets crashes

class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs["model"]



my_car = Car(make="Kia", model="Spectre")
print(my_car.make)
