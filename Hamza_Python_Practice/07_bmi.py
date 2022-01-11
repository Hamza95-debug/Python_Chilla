weight=input("Enter your weight in kg: ")
height=input("Enter your height in meters: ")
name=input("What is your name? ")
weight=float(weight)
height=float(height)
bmi= weight/height**2
print("My name is ", name, "My BMI is ", bmi)