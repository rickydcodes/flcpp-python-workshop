# Python for C++ Programmers
Guided notes for our Python workshop on 11-18-26. You already know how to program from C++, so today is about how Python says the same things. By the end you should be able to read and write basic Python: variables, conditions, functions, loops, lists, dictionaries, and a simple class.

## Setup (do this before the workshop if you can)
Install Python 3 and VS Code, then run a file called hello.py.

1. Download Python 3 from **python.org/downloads**.
   * **Mac:** run the installer, then use the `python3` command.
   * **Windows:** python.org now gives you the **Python install manager** (also on the Microsoft Store), which installs Python for you. Use the `py` command. If you use the older classic installer instead, check **Add python.exe to PATH**.
2. Install **VS Code** and the **Python** extension (published by Microsoft).
3. Create a file called **hello.py** and run it from the terminal:
```
python3 hello.py
```
On Windows: `py hello.py`

Notice:
* There is no separate compile step
* `python3` checks the whole file, turns it into bytecode (a lower-level form of your code that the interpreter runs), and runs it top to bottom
* A syntax error anywhere stops the whole file, but a type error only shows up when that line actually runs
* No `main()` function is required

**Key point:** Python runs your file directly, with no separate compile step.

## Print, Input, and Comments
`print()` replaces `std::cout`, and `input()` reads from the user.

**C++:**
```cpp
#include <iostream>
// (inside main)
std::cout << "Hello, FLC++!" << std::endl;
```
**Python:**
```python
print("Hello, FLC++!")  # comments start with # (pound sign)
```
No includes, no semicolons, no `std::`. `print()` adds the newline for you.

`input()` always gives you back a **string**:
```python
name = input("What's your name? ")
print("Hi", name)
```

**Key point:** `print()` and `input()` need no setup, and `input()` always returns a string.

## Variables and Dynamic Typing
Python is **dynamically typed**: you don't declare a type. The type belongs to the value, not the variable.

**C++:**
```cpp
int age = 19;
std::string name = "Ricky";
```
**Python:**
```python
age = 19
name = "Ricky"
age = "nineteen"  # allowed: the same variable now holds a string
```
Notice:
* No type declarations
* Types are checked while the program runs, not at compile time
* A variable can hold a different type later

Check a value's type with `type()`:
```python
print(type(age))  # <class 'str'>
```
Dynamic doesn't mean anything goes. Python won't convert between unrelated types for you: `"5" + 1` is a **TypeError**.

### Basic types
| C++ | Python |
|---|---|
| `int` | `int` (no size limit) |
| `double` / `float` | `float` |
| `bool` (`true` / `false`) | `bool` (`True` / `False`, capitalized) |
| `std::string` / `char` | `str` (no separate char type) |
| `nullptr` | `None` |

### Naming
Python uses **snake_case** (lowercase words joined by underscores) for variables and functions: `user_name`, not `userName`.

### f-strings
An **f-string** (formatted string) is the easiest way to put variables inside a string. Put an `f` before the quotes and the variable in curly braces.
```python
print(f"{name} is {age} years old")
```

**Key point:** Types belong to values, not variables, and Python won't silently mix unrelated types like `str` and `int`.

## Math and Type Conversion
Most operators match C++ (`+ - * %`); a few change.

```python
7 / 2    # 3.5  -> regular division always gives a float
7 // 2   # 3    -> floor division (what int division does in C++ for positive numbers)
2 ** 3   # 8    -> exponent, no pow() needed
-7 // 2  # -4   -> rounds DOWN. C++ -7 / 2 gives -3. % differs for negatives too
```
Notice:
* There is no `++` or `--`. Use `x += 1`.
* `x++` is an error, but `++x` runs and silently does nothing

Since `input()` always returns a string, convert it before doing math:
```python
age = int(input("Age: "))
print(age + 1)
```
`int()`, `float()`, and `str()` convert between types.

**Key point:** `/` always gives a float, `//` is floor division, and input must be converted before math.

## Conditions and Indentation
**Indentation is the syntax** in Python: a colon `:` starts a block, and everything indented under it is inside the block. There are no curly braces.

**C++:**
```cpp
if (score >= 90) {
    std::cout << "A" << std::endl;
} else if (score >= 80) {
    std::cout << "B" << std::endl;
} else {
    std::cout << "Keep going" << std::endl;
}
```
**Python:**
```python
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("Keep going")
```
Notice:
* No parentheses around the condition
* `else if` becomes `elif`
* Use 4 spaces per level
* Mixing tabs and spaces causes an error, so let VS Code handle it

Logical operators are words instead of symbols:

| C++ | Python |
|---|---|
| `&&` | `and` |
| `\|\|` | `or` |
| `!` | `not` |

```python
if age >= 18 and not is_member:
    print("Sign up at the table!")
```

**Key point:** Indentation replaces braces, so if your code looks wrong, check it first.

## Functions
Functions are defined with `def`, with no return type and no parameter types.

**C++:**
```cpp
int add(int a, int b) {
    return a + b;
}
```
**Python:**
```python
def add(a, b):
    return a + b

print(add(2, 3))  # 5
```
Notice:
* A function must be defined before the line that calls it *runs*, since the file runs top to bottom
* No prototypes needed
* One function can call another that's defined below it

*(Optional, if time)* Parameters can have default values:
```python
def greet(name="friend"):
    print(f"Hello, {name}")

greet()         # Hello, friend
greet("Ricky")  # Hello, Ricky
```

**Key point:** `def name(params):` plus an indented body. No types, no prototypes.

## Loops
`while` works like C++, with a colon and indentation. `for` is the one that changes.

```python
count = 3
while count > 0:
    print(count)
    count -= 1
```
Python's `for` loops **over a collection** (like C++'s range-based for loop). To count, use `range()`.

**C++:**
```cpp
for (int i = 0; i < 5; i++) {
    std::cout << i << std::endl;
}
```
**Python:**
```python
for i in range(5):  # 0, 1, 2, 3, 4
    print(i)
```
Notice:
* `range(start, stop, step)` stops **before** `stop`, just like `i < 5`
* `break` and `continue` work the same as C++

**Key point:** `for` walks a collection, and `range()` makes the numbers when you need to count.

## Lists
A **list** is Python's version of a vector: it grows and shrinks, and it can hold mixed types.

**C++:**
```cpp
std::vector<int> nums = {3, 1, 2};
nums.push_back(4);
```
**Python:**
```python
nums = [3, 1, 2]
nums.append(4)
print(len(nums))  # 4
print(nums[0])    # 3
print(nums[-1])   # 4  -> negative index counts from the end
```
Loop over a list directly, with no index needed:
```python
for n in nums:
    print(n)
```
**Careful:** `b = nums` does **not** copy the list like assigning a `std::vector` would. Both names point to the same list. Use `b = nums.copy()`.

*(Optional, if time)* **Slicing** takes a piece of a list (or a string): `nums[1:3]` gives the items at index 1 and 2.

**Key point:** A list is a growable vector, and assignment shares it instead of copying it.

## Dictionaries
A **dictionary** (dict) stores key-value pairs, like `std::unordered_map`, except a dict remembers the order you added keys (it is not sorted like `std::map`).

```python
member = {"name": "Ricky", "role": "co-president"}
print(member["name"])        # Ricky
member["year"] = 2           # add a new key

for key, value in member.items():
    print(f"{key}: {value}")
```

## Classes
In Python, **everything is an object**, even ints and strings (that is why they have methods like `"hi".upper()`). A class is how you make your own.

**C++:**
```cpp
class Member {
public:
    std::string name;
    int points;

    Member(std::string n) : name(n), points(0) {}

    void addPoints(int p) {
        points += p;
    }
};
```
**Python:**
```python
class Member:
    def __init__(self, name):
        self.name = name
        self.points = 0

    def add_points(self, p):
        self.points += p

ricky = Member("Ricky")   # no "new" keyword
ricky.add_points(10)
print(ricky.points)       # 10
```
Notice:
* `__init__` is the constructor
* `self` is like `this` in C++, but you write it as the first parameter of every method
* Attributes are created by assigning to `self.something` inside `__init__`, not declared at the top
* There's no `public` / `private`. By convention, a name starting with an underscore (`_points`) means "treat this as private"

**Key point:** Define the constructor as `__init__`, and always write `self` as the first parameter.

## Final Notes
* Python trades C++'s explicit types and braces for readability.
* When you're unsure what something is, `print(type(x))` it.
* For quick reference on any topic, use **w3schools.com/python**.
