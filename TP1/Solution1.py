#My Code
name =input("Enter Your Name : ")
age = int(input("Enter Your Age : "))
major = input("Enter Your Major : ")
gpa = float(input("Enter Your GPA : "))

print("EXPECTED OUTPUT")
print("=========Student Information========")
print("Name : ", name)
print("Age : ", age)
print("Major : ", major)
print("GPA : ", gpa)
print("____________________________________")

#Teacher's Code
# ---------------------------------------------------------------------------
# Problem 1 (Easy) · Student profile card
# ---------------------------------------------------------------------------
name = "Sok Dara"
age = 20
major = "Data Science"
gpa = 3.67
is_scholar = True

print("=" * 30)
print(f"Name    : {name}")
print(f"Age     : {age}")
print(f"Major   : {major}")
print(f"GPA     : {gpa:.2f}")
print(f"Scholar : {is_scholar}")
print("=" * 30)
for value in (name, age, major, gpa, is_scholar):
    print(repr(value), "->", type(value).__name__)
