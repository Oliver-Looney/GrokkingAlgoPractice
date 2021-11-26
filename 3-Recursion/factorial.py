def factorial(x):
    print("compute factorial of {0}".format(str(x)))
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


print(factorial(5))
