centuries = int(input())

cent = centuries * 100
years = int(cent * 365.2422)
days = years * 24
hours = days * 60

print(f"{centuries} centuries = {cent} years = {years} days = {days} hours = {hours} minutes")
