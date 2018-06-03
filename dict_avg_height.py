data=[{'height': 173, 'first_name': 'John', 'last_name': 'Doe'},
      {'height': 165, 'first_name': 'Sue', 'last_name': 'Norman'},
      {'height': 183, 'first_name': 'John', 'last_name': 'Davis'},
      {'height': 170, 'first_name': 'Angelina', 'last_name': 'Jolie'}]

avg_height=0
count=0

for record in data:
    avg_height+=record['height']
    count+=1

print('Średnia wzrostu wynosi :', avg_height/count)
print('Średnia wzrostu wynosi :', avg_height/len(data))

heights_by_name={}

for record in data:
    if record['first_name'] in heights_by_name:
        heights_by_name[record['first_name']].append(record['height'])
    else:
        heights_by_name[record['first_name']]= [record['height']]
print(heights_by_name)

for name, heights in heights_by_name.items():
    print(name, sum(heights)/len(heights))