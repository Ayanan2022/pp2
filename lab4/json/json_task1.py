import json
with open("/Users/ayananauryzbaeva/Desktop/pp2/labky/lab4/json/s.json","r") as f:
    data = json.load(f)

print('Interface Status')
print('=' * 80)
print('{:<50}{:<25}{:<8}{}'.format('DN', 'Description', 'Speed', 'MTU'))

print('-' * 49, '-'*24, '-'*6, '-'*5)


for row in data['imdata']:
    dn = row['l1PhysIf']['attributes']['dn']
    desc = row['l1PhysIf']['attributes']['descr']
    speed = row['l1PhysIf']['attributes']['speed']
    mtu = row['l1PhysIf']['attributes']['mtu']
    print('{:<50}{:<25}{:<8}{}'.format(dn, desc, speed, mtu))