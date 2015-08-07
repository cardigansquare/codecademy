#codeacademy function to determine if positive int is a prime number
#TODO: there's gotta be a better way to do this...
def is_prime(x):
    print x
    b_prime = True
    if x == 0 or x == 1 or x < 0:
        b_prime = False
    elif x > 3:
        for n in range(2, x):
            print n
            if (x % n == 0):
                b_prime = False
                break
    return b_prime
print is_prime(-10)