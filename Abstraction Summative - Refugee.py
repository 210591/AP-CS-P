score = 0
from random import randint
name = input("What's your name?  ")
print("Welcome", name, "to the Refugee Placement System!")
country = "spaceholder"

#All questions for the refugee acceptance follow here

def question1():
    global country
    print("What Country would you like to go to?")
    country = input("Enter Country Name: ")
    print("You have selected to go to", country + ".", "an official from",country,"will meet with you soon to interview you.")

def introOfficial():
  global country
  print("Hi, I am the immigration official from", country + ",", "I'll be asking you some questions, please just answer with 'yes' or 'no.'")

def question2():
    global score
    print("Have you ever commited a crime?")
    crime = input("Yes/No")
    crime = crime.lower()
    if crime == "yes":
        score = score + 1
        print("Was it a violent crime? This includes murder, assault, and rape")
        violent = input("Yes/No")
        violent = violent.lower()
        if violent == "yes":
            score = score + 4

def question3():
    global score
    global country
    print("Do you have any college education?")
    college = input("Yes/No")
    college = college.lower()
    if college == "no":
        print("Do you plan to go to college if allowed into", country)
        college = input("Yes/No")
        college = college.lower()
        if college == "no":
            score = score + 2

def question4():
    global score
    global country
    print("If allowed into", country, "Do you plan to work and get a job?")
    job = input("Yes/No")
    job = job.lower()
    if job == "no":
        score = score + 2

def finale():
    global score
    global country
    if score >= 5:
        print("After overlooking everything, unfortunately we can't offer you entrance to", country,"at this time")
        print("Sorry about this, and best of luck for the future")
    elif score == 4:
        print("We will consider your application, please wait...")
        acceptance = randint(1,8)
        print(acceptance)
        if acceptance >=5:
            print("You've been accepted in!")
        else:
            print("After overlooking everything, unfortunately we can't offer you entrance to", country,"at this time")
            print("Sorry about this, and best of luck for the future")
    else:
        print("Well, after looking over everything, it all seems good!")
        print("Expect your visa to", country, "in a day or two!")
        print("Best of luck moving forward,", name)

#refugee interview runs through the quiz() function

def quiz():
    question1()
    introOfficial()
    question2()
    question3()
    question4()
    finale()
quiz()
