#import math lib

# Primitive Types aka immutable objects stored in the heap
String1 = "name"
int1 = 3
float1 = 3.3
bool1 = True
# None is when no return val or particular val indicated
complex = 4+3j

# Mutable objects
# lists , dict, set, byteArray




#Lists

friends = ['Adham','Sam','Amir','Jawad']
lucky_numbers = [2,3 ,4,4,5,6,7]
print(friends)

#Basic Methods
friends.append('new friend')
friends.remove('new friend')
friends.pop()
friends.insert(1,"insertedFriend")
friends.index("insertedFriend")
friends.sort()
updated_List = friends.copy()
updated_List.extend(lucky_numbers)
friends.clear()
lucky_numbers.count(4)
print(updated_List)

# list Built in Methods
#Create a new list instance parameterized with the list
reversedList = list(reversed(friends))
print(reversedList)

size = len(friends)
print(size)

sub_list = friends[3:]
print(sub_list)


#tuples
immutableList = (1,2,3,4,5,6,7)
print(immutableList)


#Prompt
x = float(input("Enter a real number to plug in f(x) = x^2 + 10x + 16 : "))
quadraticEq = pow(x,2) + 10 * x + 16
print(quadraticEq)

# Functions
def cube(x):
    return x*x*x
print(cube(3))

#if Statements & Logical Operators
is_male = True
is_tall = False

if is_male and is_tall:
    print("male and tall")
elif is_male or is_tall:
      print("male or tall")
elif not (is_male) and is_tall:
    print("You're not a male but tall")
else:
    print("you're neither male nor tall")

# if with Comp Op
def max(a,b,c):
    if(a>b and a>c):
        return a
    elif b>a and b >c:
        return b
    elif c>a and c>b:
        return c
    else:
        return -1
print(max(3,3,3))

# calc exp
operand_1 = float(input("enter your first operand: "))
operator = input('enter your operator: ')
operand_2 = float(input("enter your second operand: "))
def calc():
    match(operator):
        case "+":
            return operand_1 + operand_2
        case("-"):
            return operand_1 - operand_2
        case("*"):
            return operand_1 * operand_2
        case("**"):
            return operand_1 ** operand_2
        case("%"):
            return operand_1 % operand_2
        case("/"):
            return operand_1 / operand_2
        case _: return "invalid operator"
print(calc())


# Dictionaries

mock_product = {
    'title': 'moc product title',
    'SN': '1323828B2N',
    "Disc": 'product disc',
    "price": 99.0,
}

# Basic methods

mock_product.update({"Price":99.9})
mock_product.get("title")


# While loop
i= 0
while i <10:
    print(i)
    i+=1
print("done with the loop: "+ str(i))


# Guessing Game
secret_word = "secret"
guess = ""
guess_count = 0
guess_limit = 3
outOfGuesses = False
while guess != secret_word and not(outOfGuesses):
    if guess_count<guess_limit:
        guess = input('Guess the secret word:')
        guess_count += 1
        if guess == secret_word:
            print("You guessed the word")
        else:
            print("You guessed wrong \n you have " + str(3 -guess_count) +" guesses left")
    else :
        print("Your out of guesses, You Lose")
        break

# For Loop

for i in range(3,len(friends)):
    print(friends[i])

# Exponent Functions
def raise_to_power(base, exponent):
    result = 1;
    for i in range(exponent):
        result *=base
    return result

result = raise_to_power(3,3)
print(result)


# 2D lists n nested Loops

number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
print(number_grid[0][0])

for row in number_grid:
    for col in row:
        print(col)

# Building a Translator
def translate(phrase):
    translation = ''
    for letter in phrase:
        if letter.lower() in 'aeiou':
            if(letter.isupper()):
                translation += "G"
            else:
                translation = translation + "g"

        else :
            translation += letter
    return translation
translation = translate(input("Enter a phrase: "))
print(translation)


# Comments

# This is a single line comment
'''
This is a multiline comment
'''


# Try n Except Statements

try:
    answer = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)

# Reading files
employees_file = open("Files I&O Manipulation/employees.txt", "r")
for employee in employees_file.readlines():
    print(employee)
employees_file.close()

# Writing to files
employees_file_w = open("Files I&O Manipulation/employees.txt", "a")
employees_file_w.write("\nRakan - Human Resources")
employees_file_w.close()

#Overriding a file we use w not a
# We can create an html file n write html
# app_content = open("app_content.html","w")
# app_content.write("<!DOCTYPE html>"
#                   "\n <html>"
#                   "\n   <head>"
#                   "\n       <meta charset='utf-8'>"
#                   "\n          <title>"
#                   "\n               Html Documentation"
#                   "\n           </title>"
#                   "\n    </head>"
#                   "\n    <body>"
#                   "\n    </body>"
#                   "\n </html>"
# )

# Modules & Pip
from mockExternalLib.module import get_file_ext as get_ext
ext1 =get_ext("Files I&O Manipulation/employees.txt")
print(ext1)
#install modules from external libs using pip
#pip install mocklib (used in terminal by using git or powershell any type of terminal)


# Classes n Objects
from Classes.Student import Student
student1 = Student("Salman","CS",4,False)
print(student1.major)


# Building a Multiple Choice Quiz

from Classes.Question import Question

question_prompts = [
    "What color are apples?\n(a) Red/Green \n(b) Yellow \n(c) Orange\n(d) Purple \n\n",
    "What color are Bananas?\n(a) Teal \n(b) Magenta \n(c) Yellow \n\n",
    "What color are strawberries?\n(a) Yellow \n(b) Red \n(c) Blue \n\n",
]

questions = [
    Question(question_prompts[0],"a"),
    Question(question_prompts[1],"c"),
    Question(question_prompts[2],"b"),
]
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if(answer == question.answer):
            score += 1
    return "You scored " + str(score) + " out of " + str(len(questions)) + " questions"


print(run_test(questions))


# Object Functions
student2 = Student("Adham","Physiotherapist", 3.4,True)
print(student2.on_honor_roll())


#Inheritance
#ChineseChef inherits from Class Chef & Overrides its special dish method
from Classes.ChineseChef import ChineseChef

myChef = ChineseChef()
myChef.make_special_dish()

# Python Interpreter
#install python to os path variable
# use from terminal for messing around without setting up an env