print(','.join(['a','b','c']))
print ('a' + ','+'b' + 'c')

def split2(text,sep):
    parts=[]
    current_part=[]
    for char in text:
        if char != sep:
            current_part.append(char)
        else:
            parts.append(''.join(current_part))
            current_part = []
    parts.append(''.join(current_part))
    return parts


print(split2('mama/goga/matonoga', '/'))
