print("Task 1")
def creatingandcalculating(text):
    try:
        number = int(text)
        result = number + 5
    except ValueError:
        try:
            number = float(text)
            result = number * 2
        except ValueError:
            return "Invalid input: This text is not number"
    result_text = "The result is: " + str(result)
    return result_text

text = "123"
result = creatingandcalculating(text)
print(result)

print("Task 2")
def arifmetic_operation(text1, text2):
    try:
        number1 = float(text1)
        number2 = float(text2)
        sum = number1 + number2
        difference = number1 - number2
        multiplication = number1 * number2
        division = number1 / number2
        result_text = "Sum: " + str(sum) + ", Difference: " + str(difference) + ", Multiplication: " + str(multiplication) + ", Division: " + str(division)
    except ValueError:
        return "Invalid input: This text is not number"
    except ZeroDivisionError:
        return "Division by zero"
    return result_text

text_number1 = "145"
text_number2 = "12"
result = arifmetic_operation(text_number1, text_number2)
print(result)
