import sys
import math

number_flights = int(input())
flights_count = number_flights
amount_flights = 0

last_flight = ''
last_1flight = ''
tot_pass = 0
max_pass = -sys.maxsize

while flights_count > 0:
    flight_name = input()
    last_flight = flight_name
    while True:
        flights = input()
        if flights == 'Finish':
            break
        else:
            amount_flights += 1
            tot_pass += int(flights)

    tot_pass = tot_pass / amount_flights

    if tot_pass > max_pass:
        max_pass = tot_pass
        last_1flight = flight_name
        print(f'{last_flight}: {math.floor(max_pass)} passengers.')
        tot_pass = 0
        amount_flights = 0
    else:
        print(f'{last_flight}: {math.floor(tot_pass)} passengers.')
        tot_pass = 0
        amount_flights = 0

    flights_count -= 1

print(f'{last_1flight} has most passengers per flight: {math.floor(max_pass)}')
