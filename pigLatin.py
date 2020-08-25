# Write a program that reads a line of text from the user. Then your program should
# translate the line into Pig Latin and display the result. Youmay assume that the string
# entered by the user only contains lowercase letters and spaces.

def get_pig_latin(words):
    # Creating one empty string where I will pass new pig latin string
    new_word = ''
    w = words.lower()
    if w[0] in ('a','e','i','o','u'):
        new_word = words + 'way'
    elif w[0] not in ('a','e','i','o','u'):
        for x in range(len(words)):
            if w[x] in ('a','e','i','o','u'):
                print('Value of x is: ', x)
                new_word = w[x:] + w[0:x-1] + 'ay'
                break
            else:
                continue
    print('New Pig Latin word is: ', new_word.capitalize())

# get_pig_latin('Computer')
