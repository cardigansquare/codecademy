#Define a function called product that takes a list of integers as input and returns the product of all of the elements in the list.
def product(integers):
    total = 1
    for i in integers:
        total *= i
    return total
print product([4, 5, 5, 5])