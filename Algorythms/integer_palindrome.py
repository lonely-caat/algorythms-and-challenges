def is_palindrome(x: int) -> bool:
    return str(x) == str(x)[::-1]


print(is_palindrome(123321))
