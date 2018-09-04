def one():
    s = input('Enter some words, letters, phrases, or sentences: ')
    c = [ord(c) for c in s]
    print("Our denary based ASCII codes for this are:",c)


def two():
    inject = input("Enter a binary number! ")
    output = int(inject, 2)
    print(output)



def start():
    inp = int(input("What would you like to convert? (ASCII Converter = 1, Binary to Denary = 2, Denary to Binary = 3, Binary to ASCII = 4"))
    if inp == 1:
        one()
    elif inp == 2:
        two()
start()
