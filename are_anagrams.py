"""def histogram(text):
    hist={}
    for char in text.lower():
        if char.isalpha():
            hist[char] = hist.get(char,0) +1
        else:
            hist['others'] = hist.get('others', 0) +1
    return hist


print(histogram('Aaaa123134bbbb12'))

"""
def are_anagrams(first,second):
    anagram_f={}
    anagram_s={}
    for char in first.lower():
        anagram_f[char]= anagram_f.get(char, 0) + 1

    for char in second.lower():
        anagram_s[char]=anagram_s.get(char, 0) + 1

    if anagram_f = anagram_s
        return True
    else:
        return False

first='ala ma kota'
second='ania ma kota'

print(are_anagrams(first,second))

def are_anagrams2(first,second):
    hist_first={}
    for char in first:
        hist_first[char] = hist_first.get(char, 0) + 1
    hist_second={}
    for char in second:
        hist_second[char] = hist_second.get(char, 0) + 1

    return hist_first == hist_second

