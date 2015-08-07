#Write a function remove_duplicates that takes in a list and removes elements of the list that are the same.
def remove_duplicates(numbers):
    new_numbers = []
    for n in numbers:
        if not (n in new_numbers):
            new_numbers.append(n)
    return new_numbers
print remove_duplicates([1,1,2,2])