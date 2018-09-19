def reverse_string_by_word(s):
    lst = s.split()  # split by blank space by default
    return ' '.join(lst[::-1])


s = 'Power of Love'
print(reverse_string_by_word(s))
# Love of Power

s = 'Hello World!'
print(reverse_string_by_word(s))
# World! Hello