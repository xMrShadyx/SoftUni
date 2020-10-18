employees = input().split(" ")
happiness_facotr = int(input())

employees = [int(emp) * happiness_facotr for emp in employees] #after mapping
average = sum(employees) / len(employees)  # Avrg. Happyness
happy = [total for total in employees if total >= average] # After Filtration

# print(employees)
# print(happy)

if len(happy) >= len(employees) / 2:
	print(f"Score: {len(happy)}/{len(employees)}. Employees are happy!")
else:
	print(f"Score: {len(happy)}/{len(employees)}. Employees are not happy!")