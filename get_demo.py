example = {'a': 1, 'b': 2, 'c': 3}
print(example.get('d',5))

data=[{'height': 173, 'first_name': 'John', 'last_name': 'Doe'},
      {'height': 165, 'first_name': 'Sue', 'last_name': 'Norman'},
      {'height': 183, 'first_name': 'John', 'last_name': 'Davis'},
      {'height': 170, 'first_name': 'Angelina', 'last_name': 'Jolie'}]


total_by_name={}
count_by_name={}

for record in data:
    first_name = record['first_name']
    total_by_name[first_name] = total_by_name.get(first_name, 0) + record['height']
    count_by_name[first_name] = count_by_name.get(first_name, 0) + 1

for name, total in total_by_name.items():
    print(name, total / count_by_name[name])
