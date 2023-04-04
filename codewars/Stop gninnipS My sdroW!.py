def spin_words(sentence):
    lst = sentence.split()
    lst = [x[::-1] if len(x) >= 5 else x for x in lst]
    return  " ".join(lst)

print(spin_words("a is string letter Spaces Kata and be that one all or of with but this with be but Write when in like or': 'a is gnirts rettel secapS Kata and be that one all or of with but this with be but Write when in like or' should equal 'a is gnirts rettel secapS Kata and be that one all or of with but this with be but etirW when in like or"))