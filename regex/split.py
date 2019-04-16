str = 'a b   c'.split(' ')
print(str)


# 无法识别连续的空格，使用正则如下
import re
newstr = re.split(r'\s+','a b   c')
print(newstr)

# multistr = re.split(r'[\s\,]+','a,b,  c  d')
multistr = re.split(r'[\s\,\;]+','a,b,  c  d')
print(multistr)








