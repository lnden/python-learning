# 使用list存储数据时，桉索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低

from collections import deque
q = deque(['a','b','c'])
# 添加最后一个元素
q.append('x')
# 添加左侧一个元素
q.appendleft('y')
# 删除最后一个元素
q.pop()
# 删除左侧第一元素
q.popleft()
print(q)