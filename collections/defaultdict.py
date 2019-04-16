# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
from collections import defaultdict
dd = defaultdict(lambda:'N/A')
# dd = {}
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])