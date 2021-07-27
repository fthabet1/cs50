import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: Invalid input.")
    print("Exiting Program...")
    sys.exit(1)
try:
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    print("Exiting Program...")
    sys.exit(1)

print(f"{x} / {y} = {result}")
