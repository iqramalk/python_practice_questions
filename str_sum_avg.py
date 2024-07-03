def calculate_sum_average(numbers):
    num_list=numbers.split()
    num_list=[int(num) for num in numbers if num.isdigit()]
    if num_list:
        total_sum= sum(num_list)
        average= total_sum/ len(num_list)
        return total_sum ,average
    else:
        return 0,0
    
input_number=input("Enter numbers with spaces = ")
total_sum , average= calculate_sum_average(input_number)
print (f" The Total Sum of Given Numbers {total_sum}")
print (f"The Average of Given Numbers is {average} ")
    