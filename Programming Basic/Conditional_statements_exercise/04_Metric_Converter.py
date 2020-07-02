number = float(input())
input_data = input()
output_data = input()


if input_data == 'mm' and output_data == 'm':
    number = number / 1000
if input_data == 'm' and output_data == 'mm':
    number = number * 1000
elif input_data == 'm' and output_data == 'cm':
    number = number * 100
elif input_data == 'cm' and output_data == 'mm':
    number = number * 10
elif input_data == 'mm' and output_data == 'cm':
    number = number / 10
elif input_data == 'cm' and output_data == 'm':
    number = number / 100

print(f'{number:.3f}')
