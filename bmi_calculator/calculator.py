def calculate_bmi(weight_kg, height_m):
    try:
        bmi = weight_kg/(height_m ** 2)
        return round(bmi, 2)
    except ZeroDivisionError:
        return None
    
def classify_bmi(bmi):
    if bmi is None:
        return "Invalid input", "height cannot be zero"
    elif bmi < 18.5:
        return "Underweight", "Nutrition tips: inccrease healthhy calories with nuts and avacados."
    elif 18.5 <= bmi < 25:
        return "Normal weight", "Great job! Maintain a healthy diet and regular exercise."
    elif 25 <= bmi < 30:
        return "Overweight", "Focus on portion control and cardio exercises."
    else:
        return "Obese", "Consult a doctor for a weight management plan."


def main():
    print("===BMI Calculator===")

    while True:
        try:
            weight = float(input("Enter your weight in kg:"))
            height = float(input("Enter your height in meters:"))

            if weight <=0 or height <= 0:
                print("Error: Weight and height must be positive\n")
                continue


            bmi = calculate_bmi(weight, height)
            category, advice = classify_bmi(bmi)

            print(f"\n Your BMI: {bmi:.2f}")
            print(f"Category:{category}")
            print(f"Recommendations:{advice}\n")

        except ValueError:
            print("Error: Invalid input! Please enter a valid number")

        another = input("\nCheck another person?(y/n:)").lower()
        if another != "y":
            print("\nThank you for using the BMI Health Advisor! Stay healthy")
            break

if __name__ == "__main__":
    main()   