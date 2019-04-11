names = ['Michael','Bob','Tracy']
scorse = [95, 75, 85]

d = {'Michael': 95,'Bob': 75,'Tracy': 85}
print(d['Michael'])

d['Animal'] = 66

print(d['Animal'])

print('Thomas' in d)

print(d.get('Thomas'))

print(d)
print(d.pop('Bob'))
print(d)