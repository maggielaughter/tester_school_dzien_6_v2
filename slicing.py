text = 'Quick brown fox'

print(text[::-1])

def split(text,sep):
    start=0
    curr=0
    parts=[]
    for char in text:
        if char != sep:
            curr += 1
        else:
            parts.append(text[start:curr])
            start=curr+1
            curr+= 1

    parts.append(text[start:curr])
    return parts


print(split('mama/goga/stonoga', '/'))

def split2(text,sep):
    parts=[]
    start=0

    for current, char in enumerate(text):
        if char == sep:
            parts.append(text[start:current])
            start = current + 1
    parts.append(text[start:])
    return parts

print(split2('mama/goga/stonoga', '/'))