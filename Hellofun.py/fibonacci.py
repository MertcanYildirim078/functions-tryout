# def getallenreeks(n1=1,n2=2,n3=3,n4=5,n5=8,n6=13,n7=21,n8=34,n9=55,n10=89):
#     n1 + n1
#     n2 + n1
#     n3 + n2
#     n4 + n3
#     n5 + n4
#     n6 + n5
#     n7 + n6
#     n8 + n7
#     n9 + n8
#     n10 + n9
def fib(getal):
    
    previousgetal = 0
    nextgetal = 1
    for x in range(getal):
        fibonacci = previousgetal + nextgetal
        previousgetal = nextgetal
        nextgetal = fibonacci
        
    return fibonacci
result = fib(1)
print(result)





