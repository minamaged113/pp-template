def greetings():
    print("Hello World!")
    return

def fibonacci(nterms):
    # Program to display the Fibonacci sequence up to n-th term
    # first two terms
    n1, n2 = 0, 1
    count = 0
    # check if the number of terms is valid
    if nterms <= 0:
        pass
    elif nterms == 1:
        print(n1)
    else:
        while count < nterms:
            print(n1)
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1