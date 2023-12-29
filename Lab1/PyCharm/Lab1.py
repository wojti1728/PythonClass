
def fib(n):
    result=[]
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

if __name__ == '__main__':
    print("Hello World")

    print(fib(10000000))

    list(range(3,6))
    # short
    # int - 4 bajty = 32bity
    #long int -