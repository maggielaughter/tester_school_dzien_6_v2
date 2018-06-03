device_names = {1: 'cpu0', 2:'mem_bank0', 3: 'mem_bank1'}
device_models = {1: 'Xeon', 2:'Corsair', 3:'Corsair'}

"""lista=[{'id': 1, 'name': 'cpu0', 'model': 'Xeon'},
       'id': 2, 'name': 'mem_bank0', 'model': 'Corsair']}"""

"""Do drugiego przykładu {'Xeon': ['cpu0'], 'Corsair':['mem_bank0', 'mem_bank1']}"""

lst=[]

for dev_id, name in device_names.items():
    model = device_models[dev_id]
    lst.append({'id':dev_id, 'name':name, 'model': model})
print(lst)
print('-----------------------------------------------------------------')

lst2={}
##drugie polecenie
for dev_id, model in device_models.items():
    name = device_names[dev_id]
    if model in lst2:
        lst2[model].append(name)
    else:
        lst2[model] = [name]
print(lst2)

