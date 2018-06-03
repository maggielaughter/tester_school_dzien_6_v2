def count_chars(text):
    count_dict={}
    for char in text:
        if char.isalpha() and char == char.upper():
            count_dict['upper']=count_dict.get('upper',0) +1
        elif char.isalpha() and char == char.lower():
            count_dict['lower']=count_dict.get('lower',0) +1
        else:
            count_dict['digit']=count_dict.get('digit',0) +1
    return count_dict

print(count_chars('OneTwo3'))