data=[{'height': 173, 'first_name': 'John', 'last_name': 'Doe'},
      {'height': 165, 'first_name': 'Sue', 'last_name': 'Norman'},
      {'height': 183, 'first_name': 'John', 'last_name': 'Davis'},
      {'height': 170, 'first_name': 'Angelina', 'last_name': 'Jolie'}]

total_by_name={}
count_by_name={}

for record in data:
    first_name = record['first_name']
    if first_name in total_by_name:
        total_by_name[first_name] += record['height']
        count_by_name[first_name] += 1
    else:
        total_by_name[first_name] = record['height']
        count_by_name[first_name] = 1

for name, total in total_by_name.items():
    print(name, total / count_by_name[name])

