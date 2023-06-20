import sqlite3
import datetime
import re

colors = {
        "PURPLE": '\033[95m',
        "CYAN": '\033[96m',
        "DARKCYAN" : '\033[36m',
        "BLUE" : '\033[94m',
        "GREEN" : '\033[92m',
        "YELLOW" : '\033[93m',
        "RED" : '\033[91m',
        "BOLD" : '\033[1m',
        "UNDERLINE" : '\033[4m',
        "END" : "\033[0m"
}

conn = sqlite3.connect('student_database_v1.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS students
              (Name text,
              Surname text,
              Number text,
              Gender text,
              Birth_Date text,
              Birth_Place text,
              E_mail text,
              Major text,
              Register_Year text)''')

print(colors["GREEN"]+"Welcome to register screen.",colors["END"])

print(colors["GREEN"]+"Step 1/9",colors["END"])
name = str(input("Enter your name: "))
while not name.isalpha():
    name = str(input("Name can only contain letters. Try again: "))

print(colors["GREEN"]+"Step 2/9",colors["END"])
surname = input("Enter your surname: ")
while not surname.isalpha():
    surname = str(input("Surname can only contain letters. Try again: "))

print(colors["GREEN"]+"Step 3/9",colors["END"])
number = input("Enter your number: ")
while not number.isnumeric():
    number = str(input("Number can only contain numbers. Try again: "))

print(colors["GREEN"]+"Step 4/9",colors["END"])
gender_codes = ["M","F"]
gender = str(input("Enter your gender, Male[M] Female[F]: "))
while gender.upper() not in gender_codes:
    gender = str(input("Gender code is incorrect, try again, Male[M] Female[F]: "))
if gender == "M":
    gender = "Male"
elif gender == "F":
    gender = "Female"

print(colors["GREEN"]+"Step 5/9",colors["END"])
error_message = ""
while True:
    user_input = input(error_message  + "Enter your birth date: (YYYY-MM-DD): ")
    components = user_input.split('-')
    if len(components) != 3:
        error_message = "Date is incorrect, YYYY-MM-DD is proper format. "
        continue
    
    integer_components = [int(c) for c in components]

    try:
        birth_date = datetime.date(*integer_components)
    except ValueError as e:
        error_message = str(e)
        continue
    break

print(colors["GREEN"]+"Step 6/9",colors["END"])
birth_place = input("Enter your birth place: ")
while not birth_place.isalpha():
    dogum_place = str(input("Birth place can only contain letters. Try again: "))

print(colors["GREEN"]+"Step 7/9",colors["END"])
e_mail = input("Enter your E-mail account: ")
 
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
 
def check(e_mail):
    while not (re.fullmatch(regex, e_mail)):
        e_mail = input("E-mail account is invalid, try again: ")
    else:
        print(colors["CYAN"]+"Email account is valid.",colors["END"])
check(e_mail);
 
print(colors["GREEN"]+"Step 8/9",colors["END"])
major = input("Enter your Major: ")

print(colors["GREEN"]+"Step 9/9",colors["END"])
birth_year = input("Enter your register date: ")
while not birth_year.isnumeric():
    birth_year = input("Register date can only contain numbers. Try again: ")

print(colors["GREEN"]+"Register is successful.",colors["END"])

cursor.execute("INSERT INTO students (Name, Surname, Number, Gender, Birth_Date, Birth_Place, E_mail, Major, Register_Year) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
               (name, surname, number, gender, birth_date, birth_place, e_mail, major, birth_year))

conn.commit()
conn.close()