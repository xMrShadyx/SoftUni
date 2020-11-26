import re
data = input()
# pattern = r"\d{2}([\./-])[A-Z][a-z]{2}\1\d{4}" # v.1
pattern = r"(?P<day>\d{2})(?P<separator>[\./-])(?P<month>[A-Z][a-z]{2})(?P=separator)(?P<year>\d{4})" # v.2 + v.3
dates = re.finditer(pattern, data)


# v.1
# for date in dates:
#     m_obj = date.group(0)
#     day = m_obj[0:2]
#     month = m_obj[3:6]
#     year = m_obj[-1:-5:-1][::-1]
#     print(f"Day: {day}, Month: {month}, Year: {year}")


# v.2
for date in dates:
    day = date.group(1)
    month = date.group(3)
    year = date.group(4)
    print(f"Day: {day}, Month: {month}, Year: {year}")


# v.3
# for date in dates:
#     d = date.groupdict()
#     print(f"Day: {d['day']}, Month: {d['month']}, Year: {d['year']}")

#13/Jul/1928, 10-Nov-1934, , 01/Jan-1951,f 25.Dec.1937 23/09/1973, 1/Feb/2016
