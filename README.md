# 🐍 Python Fundamentals

Internship prerequisite — documenting core Python concepts with hands-on examples.

## Overview

This repo tracks my Python learning progress, covering fundamental to intermediate concepts including data types, control flow, file handling, OOP, and error handling. Each section includes working, commented code examples.

---

## 1. Data Types & Structures

**Primitive (Immutable):** `str`, `int`, `float`, `bool`, `None`, `complex`

**Mutable Types:**
- **Lists** — ordered, changeable collections
- **Dictionaries** — key-value stores
- **Sets & ByteArrays** — unique values / mutable byte sequences

```python
friends = ['Adham', 'Sam', 'Amir', 'Jawad']
friends.append('new friend')
friends.insert(1, "insertedFriend")

mock_product = {'title': 'mock product title', 'price': 99.0}
mock_product.get("title")
```

**Tuples (Immutable):**
```python
immutable_list = (1, 2, 3, 4, 5, 6, 7)
```

---

## 2. Control Flow

**Conditionals + Logical Operators:**
```python
if is_male and is_tall:
    print("male and tall")
elif is_male or is_tall:
    print("male or tall")
else:
    print("neither")
```

**Match-Case (Calculator):**
```python
match operator:
    case "+": return operand_1 + operand_2
    case _:   return "invalid operator"
```

**Loops:**
- `while` — guessing game with limited attempts
- `for` — range iteration and nested 2D list traversal

---

## 3. Functions & Error Handling

```python
def cube(x):
    return x * x * x

def raise_to_power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result
```

```python
try:
    answer = 10 / 0
    number = int(input("Enter a number: "))
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
```

---

## 4. File I/O

```python
# Reading
with open("employees.txt", "r") as f:
    for line in f.readlines():
        print(line)

# Appending
with open("employees.txt", "a") as f:
    f.write("\nRakan - Human Resources")
```

> `with` statements auto-close files — cleaner and safer than `open/close`.

---

## 5. Object-Oriented Programming

```python
class Student:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def on_honor_roll(self):
        return self.gpa >= 3.5
```

**Inheritance:**
```python
class ChineseChef(Chef):
    def make_special_dish(self):   # overrides parent method
        print("The chef makes Peking Duck")
```

---

## 6. Modules & Pip

```python
from module import get_file_ext as get_ext
ext = get_ext("employees.txt")
```

```bash
pip install requests   # install external libraries via terminal
```

---

## Key Takeaways

| Concept | What I Learned |
|---|---|
| Mutability | Lists/dicts change in-place; strings/tuples don't |
| File Handling | Always use `with` — auto-closes files safely |
| Error Handling | Catch specific exceptions, not generic ones |
| OOP | Classes = blueprints; objects = instances |
| Inheritance | Child classes inherit and can override parent methods |
| Modules | Break code into reusable, importable files |

---

## Resources

- [Learn Python - Full Course for Beginners](https://www.youtube.com/watch?v=rfscVS0vtbw) — freeCodeCamp

## Status

✅ Core concepts covered — proceeding to NumPy, Pandas, and ML pipeline

---

*Built as part of internship prerequisite · May 2026*
