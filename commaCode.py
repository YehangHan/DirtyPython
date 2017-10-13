def commaCode(listParameters):
    res = ''
    for i in range(len(listParameters)):
        if i != len(listParameters) - 1:
            res += listParameters[i] + ', '
        else:
            res += 'and '+ listParameters[i]
    
    return res

spam = ['apples','bananas', 'tofu', 'cats','juice','orange']
print(commaCode(spam))