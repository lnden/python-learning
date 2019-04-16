# 如果没有namedtuple创建一个二位坐标就可以表示层,但是很难形象的看出tuple是用来表示一个坐标
p = (1,2)
print(p[0])


print('--------------------分割线------------------------')
# namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素
from collections import namedtuple
Point = namedtuple('Point',['x','y'])
p = Point(1,2)
print(p.x)


print('--------------------分割线------------------------')
# 可以验证创建的Point对象是tuple的一种子类
print(isinstance(p,Point))
print(isinstance(p,tuple))


print('--------------------分割线------------------------')
# namedtuple('名称',[属性list])
Circle = namedtuple('Circle',['x','y','r'])
c = Circle(12,12,6)
print(c.x)