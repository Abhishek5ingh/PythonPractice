# Write a program that displays the key presses that must be made to enter a text
# message read from the user. Construct a dictionary that maps from each letter or
# symbol to the key presses. Then use the dictionary to generate and display the presses
# for the user’s message. For example, if the user enters Hello, World! then your
# program should output 4433555555666110966677755531111. Ensure that
# your program handles both uppercase and lowercase letters. Ignore any characters
# that aren’t listed in the table above such as semicolons and brackets.

def text_mess(s):
    dict = {1:'.,?!:',2:'ABC',3:'DEF',4:'GHI',5:'JKL',6:'MNO',7:'PQRS',8:'TUV',9:'WXYZ',0:' '}
    sms = ''
    for st in s:
        for key in dict.keys():
            if st in dict[key]:
                pos = dict[key].index(st) + 1
                sms = sms + pos * str(key)
    print(sms)


text_mess('HELLO WORLD')
