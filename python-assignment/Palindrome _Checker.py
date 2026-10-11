def is_palindrome(text, left, right):
    # Base case: all characters have been checked
    if left >= right:
        return True

    if text[left] != text[right]:
        return False
    return is_palindrome(text, left + 1, right - 1)

text = "racecar"
print(is_palindrome(text, 0, len(text) - 1))
