def reverseStack(input):
    stack = []
    output = []
    for element in input:
        stack.append(element)

    for _ in range(len(stack)):
        output.append(stack.pop())

    return ''.join(output)

print(reverseStack('cats are cool'))
