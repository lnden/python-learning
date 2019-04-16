# 使用dict时，key是无序的，在对dict做迭代时，我们无法确定key的顺序
# 如果要保持key的瞬息，可以用OrderedDict

from collections import OrderedDict
d = dict([('a',1),('c',3),('b',2)])
print(d)
od = OrderedDict([('a',1),('c',3),('b',2)])
print(od)
print('没理解~')