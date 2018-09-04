print("Welcome to Arush's Address Book")
usage = 1
def use():
    global usage
    print("Would you like to: 1. Add a contact | 2. Look up a contact | 3. List all contacts | Any other number will exit the program")
    inp = int(input("Enter a number: "))
    if inp == 1:
        name = input("What is your contact's name? (Enter first and last name) ")
        age = input("Enter your contact's age: ")
        phone = input("Enter your contact's phone number: ")
        name=str(name)
        age=str(age)
        phone = str(phone)
        conString = ("Name: ",name," Age: ",age," Phone: ",phone)
        conString= "".join(conString)
        print("Your new contact's information -",conString)
        f= open("address-book.txt","a+")
        f.write(conString + "\n")
        f.close()
    elif inp == 3:
        f = open("address-book.txt", "r")
        lines = [line.rstrip('\n') for line in open('address-book.txt')]
        print(lines)
    elif inp == 2:
        f = open("address-book.txt", "r")
        reader = [line.rstrip('\n') for line in open('address-book.txt')]
        lines = f.read().split("\n")
        findCon = input("Who are you looking for? (Enter first and last name (CASE SENSITIVE)) ")
        for i,line in enumerate(lines):
            if findCon in line:
                print(reader[i])
    else:
        usage = 2
while usage == 1:
    use()
