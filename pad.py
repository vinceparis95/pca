

def printer(x,y):
    print(x+y)
#
# numbers = (1, 2, 3, 4)
# result = map(lambda x: x + x, numbers)
# print(list(result))


# numbers=(19,3)
# out = map(lambda x:x*x, numbers)
#
# print(list(out))

from functools import reduce

reducer = lambda x,y: x * y

li = [5,9,19]

print(reduce(reducer, li))




# write a map to square these. use a lambda function.
numbers = [1,2,3]

out= map(lambda x:x*x, numbers);
print(list(out))


numbers = [1,2,3,4,5,6,7,8,9]

print(numbers[::2])

class Car:
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed
car = Car('green','100mph')
print(car.speed)
