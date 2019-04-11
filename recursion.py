def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print(fact(5))


print('--------------------分割线------------------------')


L = []
n = 1
while n <= 99:
    L.append(n)
    n = n + 2
    print(n)


print('--------------------分割线------------------------')

