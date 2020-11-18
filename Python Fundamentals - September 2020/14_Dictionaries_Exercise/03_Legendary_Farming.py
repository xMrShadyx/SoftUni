materials = input().lower().split()
key_materials = {'shards': 0, 'fragments': 0, 'motes': 0}
junk_materials = {}
flag = False

while True:
    for i in range(0, len(materials), 2):
        key = materials[i + 1]
        value = int(materials[i])
        if key in key_materials:
            key_materials[key] += value
        elif key in junk_materials:
            junk_materials[key] += value
        elif key not in key_materials and key in ('shards', 'fragments', 'motes'):
            key_materials[key] = value
        else:
            junk_materials[key] = value
        if key in ('shards', 'fragments', 'motes') and key_materials[key] >= 250:
            key_materials[key] -= 250
            if key == 'shards':
                print('Shadowmourne obtained!')
            elif key == 'fragments':
                print('Valanyr obtained!')
            elif key == 'motes':
                print('Dragonwrath obtained!')
            flag = True
            break
    if flag:
        break
    materials = input().lower().split()

key_materials = dict(sorted(key_materials.items(), key=lambda s: (-s[1], s[0])))
junk_materials = dict(sorted(junk_materials.items(), key = lambda s: s[0]))

for key, value in key_materials.items():
    print(f'{key}: {value}')
for key, value in junk_materials.items():
    print(f'{key}: {value}')
