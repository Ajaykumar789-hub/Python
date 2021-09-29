def isprimenum(num):
    if num > 1: # prime number is always greater than 1
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")
    # if the entered number is less than or equal to 1
    # then it is not prime number
    else:
        print(num, "is not a prime number")


isprimenum(9)
