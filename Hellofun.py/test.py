def multiplyer(n):
    return lambda a : a * n

mytrpler = multiplyer(3)
print(mytrpler(11))