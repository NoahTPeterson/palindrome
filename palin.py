def is_palin(word):
    is_palin = True
    for i in range(len(word)):
        if word[-i - 1] == word[i]:
            pass
        else:
            is_palin = False
    return is_palin
    
print(is_palin("racecar"))   