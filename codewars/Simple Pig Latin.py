def pig_it(text):
    lst = text.split()
    return " ".join([x if not x.isalpha() else x[1:] + x[0] + "ay" for x in lst ])


print(pig_it('Quis custodiet ipsos custodes ?'))