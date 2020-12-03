import re

order = input()

pattern = r">>\b\w+<<\b\d+(\.\d+)?!\b\d+\b"
result = {'name': [], 'price': []}

while order != "Purchase":
    item = re.finditer(pattern, order)

    for i in item:
        item = re.findall(r"[^<>!]+", i.group())
        result['name'].append(item[0])
        result['price'].append(float(item[1]) * int(item[2]))

    order = input()

print("Bought furniture:")
[print(name) for name in result['name']]
print(f"Total money spend: {sum(result['price']):.2f}")
