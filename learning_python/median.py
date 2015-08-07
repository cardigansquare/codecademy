#Write a function called median that takes a list as an input and returns the median value of the list.
def median(numbers):
    numbers = sorted(numbers)
    f_median = 0.0
    if len(numbers) % 2 == 0:
        left_mid_index = (len(numbers) / 2) - 1
        right_mid_index = (len(numbers) / 2)
        f_median = (numbers[left_mid_index] + numbers[right_mid_index]) / 2.0
    else:
        center_index = int(round(len(numbers) / 2))
        f_median = numbers[center_index]
    return f_median
print median([7,12,3,1,6,5])