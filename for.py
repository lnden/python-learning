names = ['Michael','Bob','Tracy']
for name in names:
    print(name)


print('--------------------分割线------------------------')


sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)


print('--------------------分割线------------------------')


sums = list(range(101))
print(sums)


print('--------------------分割线------------------------')


sum = 0
for x in range(101):
    sum = sum + x
print(sum)


print('--------------------分割线------------------------')


sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)


print('--------------------分割线------------------------')


L = ['Bart','Lisa','Adam']
for name in L:
    print('hello ',name)


print('--------------------分割线------------------------')


n = 1
while n <= 100:
    print(n)
    n = n + 1
print('END')

# break 使用break结束当前循环

n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n = n + 1
print('END')

# continue 使用continue跳过当前这次循环，直接开始下一次循环

n = 0
while n < 10:
    n = n + 1
    if n % 2 ==0:
        continue
    print(n)