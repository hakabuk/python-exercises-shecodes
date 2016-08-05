from datetime import date

def print_age():
    firstName = input("What is your first name? ")
    lastName = input("What is your last name? ")
    yearOfBirth = input("What is your birth year? ")
    currentyear = date.today().year
    age = currentyear-int(yearOfBirth)
    print('Your initials are {0}{1} and you are {2} years old'.format(firstName[0].upper(), lastName[0].upper(), str(age)))

print_age()