🐍 Python Learning Journey
Internship prerequisite — Documenting core Python concepts with hands-on examples

📌 Overview
This repo tracks my Python learning progress. It covers fundamental to intermediate concepts including data types, control flow, file handling, OOP, and error management. Each section includes working code examples and comments.

🧱 1. Data Types & Structures
Primitive Types (Immutable)
str, int, float, bool, None, complex

Mutable Types
Lists – Ordered, changable collections

Dictionaries – Key-value stores

Sets & ByteArrays – Unique values / mutable byte sequences

Examples
python
friends = ['Adham', 'Sam', 'Amir', 'Jawad']
friends.append('new friend')
friends.insert(1, "insertedFriend")

mock_product = {'title': 'mock product title', 'price': 99.0}
mock_product.get("title")
Tuples (Immutable)
python
immutableList = (1, 2, 3, 4, 5, 6, 7)
🔀 2. Control Flow
Conditionals + Logical Operators
python
if is_male and is_tall:
    print("male and tall")
elif is_male or is_tall:
    print("male or tall")
else:
    print("neither")
Match-Case (Calculator)
python
match operator:
    case "+": return operand_1 + operand_2
    case _: return "invalid operator"
Loops
While – Guessing game with limited attempts

For – Range iteration & nested 2D list traversal

📦 3. Functions & Error Handling
Basic Functions
python
def cube(x):
    return x * x * x

def raise_to_power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result
Try-Except
python
try:
    answer = 10 / 0
    number = int(input("Enter a number: "))
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
📂 4. File I/O
Reading
python
with open("employees.txt", "r") as file:
    for employee in file.readlines():
        print(employee)
Writing / Appending
python
with open("employees.txt", "a") as file:
    file.write("\nRakan - Human Resources")
Creating HTML files
python
with open("app_content.html", "w") as file:
    file.write("<!DOCTYPE html><html>...</html>")
Note: with statements auto-close files — cleaner and safer.

🧪 5. Object-Oriented Programming
Class Definition
python
class Student:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def on_honor_roll(self):
        return self.gpa >= 3.5
Multiple Choice Quiz
python
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

# Usage
questions = [
    Question("What color are apples?\n(a) Red/Green\n", "a"),
    Question("What color are bananas?\n(c) Yellow\n", "c"),
]
Inheritance
python
class ChineseChef(Chef):          # Inherits from Chef
    def make_special_dish(self):   # Override parent method
        print("The chef makes Peking Duck")
📦 6. Modules & Pip
Custom Module Import
python
from module import get_file_ext as get_ext

ext1 = get_ext('employees.txt')
print(ext1)
External Libraries
bash
pip install requests   # Example — install via terminal
🧠 7. Key Takeaways
Concept	What I Learned
Mutability	Lists/dicts change in-place; strings/tuples don't
File Handling	Always close files or use with
Error Handling	Catch specific exceptions, not generic ones
OOP	Classes = blueprints; objects = instances
Inheritance	Child classes inherit and can override methods
Modules	Break code into reusable, importable files
🎯 Resources
Tutorial: Learn Python - Full Course for Beginners by freeCodeCamp.org

Status: ✅ Core concepts covered — ready for internship projects

📄 License
This repo is for learning & portfolio purposes.

Last updated: May 2026
Built as part of internship prerequisite
