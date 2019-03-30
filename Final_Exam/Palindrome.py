"""
Palindrome

"""

def is_palindrome(word):
    rev_word = word[::-1].lower()
    if word.lower() == rev_word:
        return True
    else:
        return False

print(is_palindrome('Deleveled'))
# This should print True
