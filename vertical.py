name=str(input("Enter any string = "))

def vertical_diadgonal_string():
    print("The vertical string is:\n")

    for char in name:
        print(char)
    print("The diagonal string is: \n")    
    for char in range(len(name)):
        print(" " * char + name[char] )

vertical_diadgonal_string()   

