# Define a function to calculate whether a given integer is a prime number.

def is_prime_number(x):
    if x >= 2:
        for y in range(2,x):
            if not ( x % y ):
                print("give number is not prime number")
    else:
	    print("give number is prime number")


is_prime_number(7);

