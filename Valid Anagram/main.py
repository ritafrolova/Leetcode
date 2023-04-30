#анаграммы 1
def func(s,t):
    if sorted(s)==sorted(t):
        return True
    return False
print(func("anagram","nagaram"))