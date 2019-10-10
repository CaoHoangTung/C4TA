def fibo(n):
    message = "Chay den so fibo thu " + str(n)
    if (n == 0 or n == 1):
        return 1
    print("Chay den fibonacci thu "+str(n))
    return fibo(n-1)+fibo(n-2)

print(fibo(7))