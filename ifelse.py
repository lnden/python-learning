
# 简单判断if
age = 20
if age >= 18:
    print('your age is',age)
    print('adult')


# 简单判断if else
age = 3
if age >= 18:
    print('your age is',age)
    print('adult')
else:
    print('your age is',age)
    print('teenager')


# 简单判断 if elif elif else
age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')


# 简单判断 if语句执行有个特点，它是从上往下判断，如果在某个判断上是True，就会立刻停止忽略剩余的elif else
age = 20
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')


# 简单判断 if判断还可以简写
x = 10
if x:
    print('True')



































