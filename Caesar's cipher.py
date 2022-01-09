alpha = 'abcdefghijklmnopqrstuvwxyz'
alphaUp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
number = int(input('Enter the number you want to move each letter on:'))
summary = ''

def changeChar(char):
    if char in alpha:
        return alpha[(alpha.index(char) + number) % len(alpha)]
    elif char in alphaUp:
        return alphaUp[(alphaUp.index(char) + number) % len(alphaUp)]
    else:
        return char

with open(r"C:\Users\Vlad\Desktop\TESTER\1Public\README.md") as myFile:
    for line in myFile:
        for char in line:
            summary += changeChar(char)

with open("output.txt", 'w') as myFile:
    myFile.write(summary)
