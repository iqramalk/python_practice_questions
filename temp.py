def celsius_to_farenheit(celsius):
    return (celsius *(9/5)) +32

def fareheit_to_celsius(farenheit):
    return (farenheit-32)*(5/9)

def covert_tempereture():
    print ("Coversion of Temperature")
    print("1.  Celsius to Farenheit ")  
    print("2.  Farenheit to Celsius ")  

    choice=int(input("Enter your choice (1 or 2)= "))
     
    if choice== 1:
        celsius=float(input("Enter the tempereature in Celsius = "))
        farenheit=celsius_to_farenheit(celsius)         #store result in a variable 
        print (f"{celsius} C is {farenheit} F")
    elif choice== 2:
        farenheit=float(input("Enter the temperetaure in Farenheit ="))
        celsius=fareheit_to_celsius(farenheit)
        print (f"{farenheit} F is {celsius} C")
    else:
        print("Invalid")

covert_tempereture()

    
     

