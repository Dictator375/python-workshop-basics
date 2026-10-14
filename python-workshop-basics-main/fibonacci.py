def fib(n):    # write Fibonacci series up to n
    """
    Print a Fibonacci series less than n.
    """
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    """
    Return a list containing the Fibonacci series up to n.
    """
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

# Executing modules as scripts
if __name__ == "__main__":
    # This only runs if we run the script
    import sys
    fib(int(sys.argv[1]))