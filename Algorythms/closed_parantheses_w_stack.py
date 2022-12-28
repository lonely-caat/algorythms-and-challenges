def is_valid(s: str):
    stack = []
    d = {'{':'}', '[':']', '(':')'}

    for element in s:
        if element in d:
            stack.append(element)

        elif element != d[stack.pop()]:
            return False

    return len(stack) == 0

print(is_valid('{()}'))




