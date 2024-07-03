print ("****Welcome to Even and Odd Checker****")

def EvenOddChecker():
    num=int(input("Enter any number = "))
    if num > 0:
        print(f"{num} is a natural number \n Let's find whether it is EVEN or ODD ")
        if num %2 ==0:
            print(f"{num} is an EVEN NUMBER")
        else:
            print(f"{num} is an ODD NUMBER")

    else:    
        print(" ERROR !!!!!!GIVEN NUMBER IS NOT NATURAL NUMBER!!!!!! ")

EvenOddChecker()   

        

             
          

