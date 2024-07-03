vowels = 0
consonants=0
input_string=input("Enter any word = ")
vowel_set={'a','A','e','E','i','I','o','O','u','U'}
for char in input_string:
    if char.isalpha():
        if char in vowel_set:
            vowels+=1
        else:
            consonants+=1


print("Total vowels in given string = " , vowels)
print("Total consonants in given string = ", consonants)                 