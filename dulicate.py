input_number=input("Enter number with spaces = ").split()
unique_num=set()
duplicates=[]
for num in input_number:
    if num in unique_num:
        duplicates.append(num)
    else:
        unique_num.add(num)
if num in duplicates:
    print("Duplicate in list are :",duplicates)
else:
    print("No dupliacte found")                 

