def return_10():
    return 10

def add(num1, num2):
    add_result = num1 + num2
    return add_result

def subtract(num1, num2):
    subtract_result = num1 - num2
    return subtract_result

def multiply(num1, num2):
    multiply_result = num1 * num2
    return multiply_result

def divide(num1, num2):
    divide_result = num1 / num2
    return divide_result

def length_of_string(string):
    string_length = len(string)
    return string_length

def join_string(line_1, line_2):
    joined_string = line_1 + line_2
    return joined_string

def add_string_as_number(num1, num2):
    add_result = int(num1) + int(num2)
    return add_result

def number_to_full_month_name(num):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return months[num-1]

def number_to_short_month_name(num):
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    return months[num-1]

def volume_of_cube(length):
    volume = length ** 3
    return volume

def reverse_string(in_string):
    reverse = in_string[::-1]
    return reverse

def fahrenheit_to_celsius(temp):
    result = (temp - 32) * 5 / 9
    return result
