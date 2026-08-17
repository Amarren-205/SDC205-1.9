name = input("Enter your name: ")
student_id = input("Enter your Student ID: ")

# Numbers that will be calculated
num1 = int(input("Enter your first whole number: "))
num2 = int(input("Enter your second whole number: "))

# Calculations
multiplication = num1 * num2
division = num1 / num2
subtraction = num1 - num2

# Calculation results for what the user chose
print("\n--- Calculation Results ---")
print(f"Multiplication: {multiplication:.2f}")
print(f"Division: {division:.2f}")
print(f"Subtraction: {subtraction:.2f}")

# Greater or less than
if num1 > num2:
    print("Your first number is larger than your second number.")
elif num1 < num2:
    print("Your first number is smaller than your second number.")
else:
    print("The two numbers are equal.")

# My info
print("\n--- Student Information ---")
print("Name: Amarren Hopkins")
print("Student ID: AMAHOP2918")
