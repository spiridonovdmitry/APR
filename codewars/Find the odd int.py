def find_it(seq):
    count = {}
    for i in seq:
        if(count.get(i)):
            count[i] += 1
        else:
            count[i] = 1
    
    for key, val in count.items():
        if (val % 2 != 0):
            return key
    return 0



find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])