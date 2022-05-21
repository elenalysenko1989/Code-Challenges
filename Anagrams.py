def is_anagram(t1, t2):
    return sorted(t1) == sorted(t2)
    
print(is_anagram('angel', 'glean'))
print(is_anagram('angel', 'devil'))