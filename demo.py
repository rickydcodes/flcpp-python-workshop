# ===== 1. Print, Input, Comments =====
print("Hello, FLC++!")

name = "Ricky"
print("Hi", name)


# ===== 2. Variables and Dynamic Typing =====
age = 19
print(type(age))
age = "nineteen"
print(type(age))

user_name = "Ricky"
age = 19
print(f"{user_name} is {age} years old")


# ===== 3. Math and Type Conversion =====
print(7 / 2)
print(7 // 2)
print(2 ** 3)
print(-7 // 2)

x = 5
++x
print(x)
x += 1
print(x)

print(int("20") + 1)


# ===== 4. Conditions and Indentation =====
score = 85
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("Keep going")

is_member = False
if age >= 18 and not is_member:
    print("Sign up at the table!")


# ===== 5. Functions =====
def add(a, b):
    return a + b

print(add(2, 3))
print(add("FLC", "++"))

def greet(name="friend"):
    print(f"Hello, {name}")

greet()
greet("Ricky")


# ===== 6. Loops =====
count = 3
while count > 0:
    print(count)
    count -= 1

for i in range(5):
    print(i)


# ===== 7. Lists =====
nums = [3, 1, 2]
nums.append(4)
print(len(nums), nums[0], nums[-1])

for n in nums:
    print(n)

b = nums
b.append(99)
print(nums)
c = nums.copy()

print(nums[1:3])


# ===== 8. Dictionaries =====
member = {"name": "Ricky", "role": "co-president"}
print(member["name"])
member["year"] = 2
for key, value in member.items():
    print(f"{key}: {value}")


# ===== 9. Classes =====
print("hi".upper())

class Member:
    def __init__(self, name):
        self.name = name
        self.points = 0

    def add_points(self, p):
        self.points += p

ricky = Member("Ricky")
ricky.add_points(10)
print(ricky.name, ricky.points)
