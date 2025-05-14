# Simple BMI Calculator

def main():
    print("BMI Calculator")
    print("==============")

    try:
        weight = float(input("Enter your weight (kg): "))
        height = float(input("Enter your height (m): "))

        if weight <= 0 or height <= 0:
            print("Error! Weight and height must be positive numbers.")
            return

    except ValueError:
        print("Invalid input! Please enter numbers only.")
        return

    bmi = weight / (height * height)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi >= 18.5 and bmi < 25:
        category = "Normal weight"
    elif bmi >= 25 and bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    print("\nResults:")
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Category: {category}")

    if category == "Underweight":
        print("You might want to check with a doctor about healthy weight gain.")
    elif category == "Overweight" or category == "Obese":
        print("It's a good idea to consult a doctor about healthy weight management.")
    else:
        print("Great! You're in a healthy range. Keep it up.")

if __name__ == "__main__":
    main()
