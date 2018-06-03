def split(text,sep):
    data=[]
    word=''
    for char in text.lower():
        if char == sep:
            data.append(word)
            word=''
        else:
            word += char
    data.append(word)
    return data

print(split('mama/goga/matonoga', '/'))


def split2(text,sep):
    parts=[]
    current_part=''
    for char in text.lower():
        if char != sep:
            current_part += char
        else:
            parts.append(current_part)
            current_part = ''
    parts.append(current_part)
    return parts


print(split2('mama/goga/matonoga', '/'))

#wynik numbers= '123,21,37,3'
#print(split(numbers,',') == ['123','21','37','3']
#print(split(numbers, '2') == ['1','3,','1,37,3']
