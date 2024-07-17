#sum of digits
number = 8391
sum_of_digits = sum(int(digit) for digit in str(number))
print(f"sum of digits {number} = {sum_of_digits}")



#reverse order
number = 9045
reversed_number = int(str(number)[::-1])
print(f"reverse order {number} = {reversed_number}")



#sorted_number
number = 8253
digits = list(str(number))
sorted_digits = sorted(digits)
sorted_number = int(''.join(sorted_digits))
print(f"sorted_number {number} = {sorted_number}")
