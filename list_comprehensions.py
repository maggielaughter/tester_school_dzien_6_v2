dev_ids = []

for i in range(1,5):
    dev_ids.append('device_' + str(i))

print(dev_ids)
#wyrażenie listowe
#składa się z : faktyczne wyrażenie + for coś tam i coś tam
print(['device_' + str(i) for i in range(1,5)])
print('-------------------------------------------------------------')
print([i**2 for i in range(2,101)])

print()
print()

lst_dict=[{'id': 1, 'model': 'Model1'},
          {'id': 2, 'model': 'Model2'},
          {'id': 3, 'model': 'Model3'},
          {'id': 4, 'model': 'Model4'},
          {'id': 5, 'model': 'Model5'},
          {'id': 6, 'model': 'Model6'}]

for item in lst_dict:
    print(item['id'])

print([item['id'] for item in lst_dict])

