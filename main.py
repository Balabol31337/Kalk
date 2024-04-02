import random

def calculate():
    num1 = float(input("Enter the first number: "))
    operator = input("Enter an operator (+-*/): ")
    num2 = float(input("Enter the second number: "))

    if operator == "+":
        answer = num1 + num2
    elif operator == "-":
        answer = num1 - num2
    elif operator == "*":
        answer = num1 * num2
    elif operator == "/":
        if num2 != 0:
            answer = num1 / num2
        else:
            print("Infinity! You broke the calculator! (Division by zero)")
            return
    else:
        print("Invalid operator!")
        return

    if random.randint(1, 10) == 7:
        print("The secret number is 7! You win a virtual cookie! 🍪")

    print(f"The answer is: {answer}")

if __name__ == "__main__":
    calculate()
