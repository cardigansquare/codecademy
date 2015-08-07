#Define a function called purify that takes in a list of numbers, removes all odd numbers in the list, and returns the result.
def purify(numbers):
    new_numbers = []
    for n in numbers:
        if n % 2 == 0:
            new_numbers.append(n)
    return new_numbers
purify([1,2,3,4,5,6,2])