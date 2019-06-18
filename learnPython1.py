print('Faizan Jamil')

names = ['Susan', 'James', 'Roger', 'Bryan', 'Jacob']
print('Size of list is: ' + str(len(names)))

ages = [16, 18, 22, 21, 20]
i = 0
j = 0
for x in names:
    print(x)

for y in ages:
    print(str(y))

while i < len(names):
    while j < len(ages):
        print('Name: ' + names[i] + ' Age: ' + str(ages[j]))    
        i+=1
        j+=1
        break