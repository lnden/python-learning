import re

correct = re.match(r'\d{3}\-\d{3,8}$','010-12345')
print(correct)

error = re.match(r'\d{3}\-\d{3,8}$','010 12345')
print(error)

print('--------------------分割线------------------------')


# match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None
test = '用户输入的字符串'
if re.match(r'正则表达式',test):
    print('ok')
else:
    print('failed')
