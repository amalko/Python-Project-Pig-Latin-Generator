
word= input("Enter a word : ")                                  # Getting an input from the user
global pig_word                                                 # declaring a global variable

# Function
def pig_latin(word):
    global pig_word
    if word[0] in 'aeiou':                                      # Checking if the first letter of the entered word is a vowel
        pig_word = word + 'ay'

    else:
        pig_word = word[1:] + word[0] + 'ay'

pig_latin(word)                                                 # Calling the function to generate pig latin 
print("Pig Latin for the given word is "+ pig_word)