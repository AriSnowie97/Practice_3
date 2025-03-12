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
