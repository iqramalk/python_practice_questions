word=str(input("Enter any Word or Sentence :"))

def vowel_consonant_summary(word):
    vowels=" aeiouAEIOU "
    
    for i in word:
        if i.isalpha():
            if i in vowels:
                print(i ," is a vowel ")
            else:
                print(i, " is  a consonant ")
        else:
            print( i ," is not a letter")

vowel_consonant_summary(word)            
        