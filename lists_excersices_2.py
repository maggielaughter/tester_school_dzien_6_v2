lst=['asd','sdf', 'sdfasdf', 'asdfqwefadf', 'sdfasdf']
lst2=[]
for item in lst:
    lst2.append((len(item)))

print(lst2)
print([(len(item)) for item in lst])