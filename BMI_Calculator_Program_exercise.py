"""
This program takes input from user and calculates user's BMI (Body Mass Index).
After calculating the BMI value, it prints out the message indicating if the person is 'Underweight', 'Normal', 'Overweight'
or 'Obese'.

Detail about BMI: https://en.wikipedia.org/wiki/Body_mass_index

BMI is calculated using a persons weight and height. BMI is 'weight' devided by square of height.

BMI = weight/(height^2)

The BMI should be classified as follows
Underweight - BMI under or equal to 18.5
Normal - BMI between 18.5 and 25 (not including 18.5 but including 25)
Overweight - BMI between- 25 and 30 (not including 25 but including 30)
Obese - BMI greater than 30

"""


print("Welcome to BMI Calculator!")

weight = input("Enter your weight in kg: ")
height = input("Enter your height in m: ")
BMI = float(weight) / float(height)**2
BMItext = round(BMI, 1)

if float(BMI) <= 18.5:
    print(f"Your BMI is {BMItext}. You are Underweight.")
elif float(BMI) > 18.5 and float(BMI) <= 25:
    print(f"Your BMI is {BMItext}. You are Normal")
elif float(BMI) >= 25 and float(BMI) <= 30:
    print(f"Your BMI is {BMItext}. You are Overweight")
elif float(BMI) > 30:
    print(f"Your BMI is {BMItext}. You are Obese")



