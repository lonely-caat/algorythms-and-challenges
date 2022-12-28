def fibo(n):
    l = [0,1]

    for elements in range(2, n):
        l.append(l[elements-1]+l[elements-2])

    return l


# def fiboRecursion(n):
#     if n < 2:
#         return 1
#     else:
#         return fiboRecursion(n-1) + fiboRecursion(n-2)
#
# l = []
# for element in range(8):
#     l.append(fiboRecursion(element))
# print(l)


def fiboRecursionMemoization(n, prevValues=[]):
    try:
        return prevValues[n]
    except IndexError:
        pass

    if n < 2:
        result =  1
    else:
        result =  fiboRecursionMemoization(n-1, prevValues) + fiboRecursionMemoization(n-2, prevValues)

    prevValues[n] = result
    return result

# l = []
# for element in range(8):
#     l.append(fiboRecursionMemoization(element))
# print(l)

print(fiboRecursionMemoization(8))