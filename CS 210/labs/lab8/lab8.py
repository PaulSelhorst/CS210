def get_vowel_count(s):
    """
    Using recursion, return the number of vowels in the string s.
    """
    if len(s) == 0:
        return 0
    if s[0] in 'aeiou':
        return 1 + get_vowel_count(s[1:])
    else:
        return get_vowel_count(s[1:])

def multiply(a, b):
    """
    Using recursion, return the product of a and b.
    """
    if a == 0 or b == 0:
        return 0
    if b < 0:
        return -a + multiply(a, b + 1)
    else:
        return a + multiply(a, b - 1)
    
def deep_reverse(a: list) -> list:
    """
    Using recursion, return a new list that is the deep reverse of a.
    """
    if len(a) == 0:
        return []
    if type(a[-1]) == list:
        return [deep_reverse(a[-1])] + deep_reverse(a[:-1])
    else:
        return [a[-1]] + deep_reverse(a[:-1])
        
print(get_vowel_count('hello'))
print(multiply(5, 5))