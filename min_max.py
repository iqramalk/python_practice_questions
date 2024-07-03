list_number=list(map(int ,input("Enter the list of number space between them = ").split()))
choice=input("Enter your choice for Maximum type **max** and for Minimum ** min** = ")

if choice== "max":
    max_num=list_number[0]
    for i in range(1, len(list_number)):
        if list_number[i] > max_num:
            max_num=list_number[i]
    print("The Maximim number is ", max_num)     
elif choice == "min":
    min_num=list_number[0]
    for i in range(1,len(list_number)):
        if list_number[i]< min_num:
            min_num=list_number[i]       
    print("The minimim number is ", min_num)        
else:
    print("Invalid ")