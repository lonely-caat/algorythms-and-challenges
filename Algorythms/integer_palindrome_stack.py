def integer_palindrome(integer):
    stack = []
    li = list(str(integer))
    for element in range(len(li)):
        stack.append(li.pop())

    stack = int(''.join(stack))
    return stack == integer

print(integer_palindrome(121))

