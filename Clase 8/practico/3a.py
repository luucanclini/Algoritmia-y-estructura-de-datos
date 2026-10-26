def reverse(s:list):
    if len(s) == 0:
        return []
    
    return reverse(s[1:]) + [s[0]]
vocales = ['a','e','i','o','u']
print(reverse(vocales))