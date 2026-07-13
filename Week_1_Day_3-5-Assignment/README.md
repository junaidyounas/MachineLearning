# Python Practice Worksheet

**Data Structures, Conditionals, Loops & Functions**

Practice programs for Days 3–5 of the AI & Machine Learning course. Attempt the programs in order — they progress from easier to slightly more challenging within each topic group.

---

## Overview

This assignment covers core Python fundamentals:

- Conditionals (`if`, `elif`, `else`, nested `if`, ternary operator)
- Loops (`while`, `for`, `break`, `continue`, `pass`)
- Data structures (lists, tuples, dictionaries, sets)
- Functions, scope, list comprehension, `lambda`, and `map()`

**Notebook:** [`PythonTasks_12_July.ipynb`](./PythonTasks_12_July.ipynb)

---

## Programs

### Conditionals

| # | Topic | Task |
|---|-------|------|
| 1 | If-Else | Take a number from the user and check whether it is **Even** or **Odd**. |
| 2 | If-Elif-Else | Take the marks of a student and print **Pass** (Marks ≥ 33) or **Fail** (Marks < 33). |
| 3 | Nested If | Take the student's marks and fee status. If marks ≥ 50: if fee is paid → **Admission Confirmed**, otherwise → **Fee Required**. Else → **Not Eligible**. |
| 4 | Ternary Operator | Take the user's age and print **Adult** or **Minor** using the ternary operator. |

### Loops

| # | Topic | Task |
|---|-------|------|
| 5 | While Loop | Calculate the sum of all numbers from 1 to a given number using a `while` loop. |
| 6 | For Loop | Print numbers from **10 to 1** using a `for` loop. |
| 7 | Break Statement | Print numbers from 1 to 20. Stop the loop when the number becomes **9**. |
| 8 | Continue Statement | Print numbers from 1 to 20 but **skip 5 and 10**. |
| 9 | Pass Statement | Write a program showing the use of the `pass` statement inside an `if` statement. |

### Data Structures

| # | Topic | Task |
|---|-------|------|
| 10 | Lists | Take 5 numbers from the user, store them in a list, and print the complete list. |
| 11 | Lists | Take five student names in a list. Print each name using a `for` loop. |
| 12 | Tuples | Create a tuple of seven days. Print the **first day** and **last day**. |
| 13 | Dictionary | Create a dictionary of one student. Update the student's age and print the updated dictionary. |
| 14 | Sets | Create two sets. Print the **union** and **intersection**. |
| 15 | `enumerate()` | Create a list of five fruits. Use `enumerate()` to print both the index and the fruit name. |

### Advanced Topics

| # | Topic | Task |
|---|-------|------|
| 16 | Nested Loops | Print the following pattern: `*`, `**`, `***`, `****`, `*****` |
| 17 | List Comprehension | Create a list of numbers from 1 to 10. Using list comprehension, create another list containing the **squares** of those numbers. |
| 18 | Functions | Write a function that prints the **multiplication table** of a number. |
| 19 | Lambda & `map()` | Take multiple numbers from the user. Use `map()` to convert them to integers. Use a lambda to multiply every number by 2. Print the new list. |
| 20 | Variable Scope | Write a program showing the difference between a **local variable** and a **global variable**. |

---

## Program Details

### Program 1: Even or Odd (If-Else)

```python
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

### Program 2: Pass or Fail (If-Elif-Else)

```python
marks = int(input("Enter marks: "))
if marks >= 33:
    print("Pass")
else:
    print("Fail")
```

### Program 3: Admission Check (Nested If)

```python
marks = int(input("Enter marks: "))
fee_paid = input("Is fee paid? (yes/no): ").lower() == "yes"

if marks >= 50:
    if fee_paid:
        print("Admission Confirmed")
    else:
        print("Fee Required")
else:
    print("Not Eligible")
```

### Program 4: Adult or Minor (Ternary Operator)

```python
age = int(input("Enter age: "))
status = "Adult" if age >= 18 else "Minor"
print(status)
```

### Program 5: Sum with While Loop

```python
n = int(input("Enter a number: "))
total, i = 0, 1
while i <= n:
    total += i
    i += 1
print(f"Sum from 1 to {n} = {total}")
```

### Program 6: Countdown (For Loop)

```python
for i in range(10, 0, -1):
    print(i)
```

### Program 7: Break at 9

```python
for i in range(1, 21):
    if i == 9:
        break
    print(i)
```

### Program 8: Skip 5 and 10 (Continue)

```python
for i in range(1, 21):
    if i in (5, 10):
        continue
    print(i)
```

### Program 9: Pass Statement

```python
x = 10
if x > 5:
    pass  # placeholder — logic to be added later
print("Program continues after pass")
```

### Program 10: List of Numbers

```python
numbers = []
for _ in range(5):
    numbers.append(int(input("Enter a number: ")))
print(numbers)
```

### Program 11: Student Names

```python
students = ["Ali", "Sara", "Ahmed", "Fatima", "Hassan"]
for name in students:
    print(name)
```

### Program 12: Days Tuple

```python
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("First day:", days[0])
print("Last day:", days[-1])
```

### Program 13: Student Dictionary

```python
student = {"name": "Ali", "age": 20, "course": "AI"}
student["age"] = 21
print(student)
```

### Program 14: Set Operations

```python
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print("Union:", set_a | set_b)
print("Intersection:", set_a & set_b)
```

### Program 15: Enumerate Fruits

```python
fruits = ["apple", "banana", "mango", "grape", "orange"]
for index, fruit in enumerate(fruits):
    print(index, fruit)
```

### Program 16: Star Pattern (Nested Loops)

```python
for i in range(1, 6):
    print("*" * i)
```

### Program 17: Squares (List Comprehension)

```python
numbers = list(range(1, 11))
squares = [n ** 2 for n in numbers]
print(squares)
```

### Program 18: Multiplication Table (Function)

```python
def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

multiplication_table(int(input("Enter a number: ")))
```

### Program 19: Lambda and map()

```python
raw = input("Enter numbers separated by spaces: ").split()
nums = list(map(int, raw))
doubled = list(map(lambda x: x * 2, nums))
print(doubled)
```

### Program 20: Local vs Global Scope

```python
global_var = "I am global"

def demo():
    local_var = "I am local"
    print(global_var)
    print(local_var)

demo()
print(global_var)
# print(local_var)  # Uncomment to see NameError
```

---

## How to Run

1. Open [`PythonTasks_12_July.ipynb`](./PythonTasks_12_July.ipynb) in Google Colab or Jupyter.
2. Run each cell in order (Programs 1–20).
3. Enter the required input when prompted.

**Requirements:** Python 3.x (no external packages needed).

---

## Topics Covered

| Category | Concepts |
|----------|----------|
| Conditionals | `if`, `elif`, `else`, nested conditions, ternary operator |
| Loops | `while`, `for`, `range()`, `break`, `continue`, `pass` |
| Data Structures | `list`, `tuple`, `dict`, `set`, indexing, updating |
| Built-ins | `enumerate()`, `map()`, `input()`, `int()` |
| Functions | Defining functions, parameters, local vs global scope |
| Advanced | Nested loops, list comprehension, lambda expressions |
