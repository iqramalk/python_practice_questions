print("Fabonnaci Series of any integer number:\n")

def fabonacci_series(n):

    a,b=0,1
    print(a,b ,end=" ")
    for _ in range(2,n):
        c=a+b
        print(c ,end=" ")
        a ,b=b,c
    

n=int(input("Enter an integer term = "))
print("Fabonacci Series of ", n ,"term is :")
fabonacci_series(n)
