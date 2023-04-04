

def count(s):
    dict1 = {}

    for i in s:
        if(dict1.get(i)):
            dict1[i] += 1
        else:
            dict1[i] = 1
    
    str = ""

    return dict1



print(count("aba"))