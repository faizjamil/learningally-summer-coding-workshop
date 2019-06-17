print('Faizan Jamil')

names = ['Susan', 'James', 'Roger', 'Bryan', 'Jacob']
print('Size of list is: ' + str(len(names)))

ages = [16, 18, 22, 21, 20]

for x in names:
    print(x)

for y in ages:
    print(str(y))

for x in range(0, len(ages)):
    print('Name: ' + names[x] + ' Age: ' + str(ages[x]))