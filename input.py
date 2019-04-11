

# 使用input输入生日
# input()返回的数据类型是str，str不能直接和整数比较，必须先把str转换成整数。python提供了 `int()` 函数类完成这件事情
birth = input('birth:')
if int(birth) < 2000:
    print('00前')
else:
    print('00后')

# s = input('birth:')
# birth = int(s)
# if birth
# 输入 abc 会报错，int()方法发现一个字符串并不是合法的数字时



height = 1.75
weight = 80.5
bmi = weight/(height*height)

if bmi < 18.5:
    print('过轻')
elif bmi < 25:
    print('正常')
elif bmi < 28:
    print('过重')
elif bmi < 32:
    print('肥胖')
else:
    print('严重肥胖')
