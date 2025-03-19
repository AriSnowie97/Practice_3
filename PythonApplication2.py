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
print("Task 3")
def convert_and_calulate(input_string, operation="sum"):
    try:
        numbers = [float(x) for x in input_string.split(",")]
        if operation == "sum":
            return sum(numbers)
        elif operation == "average":
            return sum(numbers) / len(numbers)
        else:
            return None
    except ValueError:
        return None
input_str = "1,2,3,4,5"
sum_result = convert_and_calulate(input_str, "sum")
average_result = convert_and_calulate(input_str, "average")
if sum_result is not None:
    print(f"Sum of numbers: {sum_result}")
if average_result is not None:
    print(f"Average of numbers: {average_result}")

error_input = "1,2,3,4,5,abc"
error_result = convert_and_calulate(error_input, "sum")
if error_result is None:
    print("Invalid input: This text is not number")
print("Task 4")
def format_float_to_string(number, decimal_places):
    formatted_string = f"{number:.{decimal_places}f}"
    return formatted_string

number = 3.14159
decimal_places = 2
result = format_float_to_string(number, decimal_places)
print(result)
