# python-learning

&emsp;&emsp;立一个flag，从今天开始学习python，作为前端开发的第二语言学习。坚持每天学习，争取实战用到WEB端

## python基础

- `#` 开始的语句是注释，可以是任意内容，解释器会忽略掉注释
- `:` 当语句以冒号:结尾时，锁紧的语句视为代码块
- 数据类型和变量

    1.整数 1、100、-8080、0

    2.浮点数  浮点数也就是小数，之所以成为浮点数，是因为按照科学记数法表示时，一个浮点数的小数点位置是可以变的

    3.字符串 字符串是以单引号''或双引号""括起来的任意文本，比如'abc' "xyz"  "I'm ok" 如果有单引号和双引号 可以使用转译\' \"

        这里python给我提供两个比较方便的方法

            1). r'adasdas\\\asdasdad' 使用r''表示内部默认不转译
            2). '''asdasdasd''' 使用'''包括起来允许多汗输出

    4.布尔值 在python中只有True、False两种，注意大写

        运算符 或||、与&&、非!  对应 python 的是 或or、与and、非not

    5.空值 空值是python里一个特殊的值，用None表示，是一个特殊的空值

    6.变量 直接声明  name = 'lily' = 是赋值语句

        python 、JavaScript属于动态类型语言，类型不确定，可以随之改变。不想java  定义好类型不允许改变 int name = 'lily'  name = "ABC"//报错

    7.常量 所谓常量就是不能变的 变量，比如常用的数学常数TT就是一个常量，在python中 全部大写

        在python中/是除法可以精确到浮点数 10/3 == 3.333333  //可以取整数10//3 == 3

    8.list 是python内置的一种数据类型是列表。

        1).len(classmates)

        2).classmates.append('jack')

        3).classmates.insert(1,'lulu')

        4).classmates.pop()     //删除最后一个

        5).classmates.pop(1)    //删除索引1

    9.tuple 另一种有序的列表叫元组，与list非常相似，但是tuple一旦初始化就能修改，比如同样是列出同学的名字

        tuple与ES6里面的const类似，一旦定义就不能随便修改，append,insert都无法使用

        但是，要定义一个只有1个元素的tuple，t = (1)  t // 1

        定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。

        所以，只有1个元素的tuple定义时必须加一个逗号,，来消除歧义： t = (1,)  t  // (1,)

        **tuple 指向不变，内部如果是list是可以改变的**

- 判断条件

    if else 后需要添加冒号: 冒号后视为语句块


- 循环

    python的循环有两种，一种是for...in循环，依次把list或tuple中的每一个元素迭代出来

- dict 字典dictionary  类似其他语言的map

    d = {'Michael': 95,'Bob': 75,'Tracy': 85}

    判断key是否存在，有两种办法

        1).通过 in 判断key是否存在  'Thomas' in d   // False
        2).通过 get() 方法， 如果key不存在，可以返回None   d.get('Thomas')  // None

    d.pop('Bob')    //  75


和list比较，dict有以下几个特点：

&emsp;&emsp;1).查找和插入的速度极快，不会随着key的增加而变慢；

&emsp;&emsp;2).需要占用大量的内存，内存浪费多。

而list相反：

&emsp;&emsp;1).查找和插入的时间随着元素的增加而增加；

&emsp;&emsp;2).占用空间小，浪费内存很少。


- set 类似dict 也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key

    s = set([1, 1, 2, 2, 3, 4])  //  {1, 2, 3}

    1). add(key) 可以添加元素到set中，可以重复添加，但不会有效果

    2). remove(key) 可以删除元素

    3). 可以看成数学意义上的无序和无重复元素的集合

        s1 = set([1, 2, 3])
        s2 = set([2, 3, 4])
        s1 & s2     //  {2, 3}
        s1 | s2     //  {1, 2, 3, 4}


## 函数

    Python不但能非常灵活地定义函数，而且本身内置了很多有用的函数，可以直接调用。

    将重复的代码封装到一个函数里面，每次调用函数生成对应的值，不用每次都求 S = πr2

- 使用函数

    1). abs() 求绝对值函数

    2). max() 求最大值函数

    3). hex() 整数转换成十六进制表示的字符串

    4). 数据类型转换

```
int('123')  //  123

int(12.34)  //  12

float('12.34')  //  12.34

str(1.23)   //  '1.23'

bool(1)     //  True

bool('')    //  False
```
    5). 函数名其实就是指向一个函数对象的引用，完全可以吧函数名赋给一个变量，相当于给这个函数起了一个"别名"

    a = abs    a(-1)    //  1

- 定义函数

    在python中，定义一个函数要使用def语句，一次写出函数名、括号、括号中的参数和冒号`：`，然后，在锁紧块中编写函数体，函数的返回值用return 语句返回

```
def my_abs(x):
    if x >=0:
        return x
    else:
        return -x
```


    1).空函数 pass 实际上就是起到占位符的作用，空函数减少pass会报错

```
age = 20
if age >= 18:
    pass
```

    2).参数检查 my_abs 和内置函数abs 是有区别的  my_abs('A') / abs('A') 报错信息

```
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
```

    3).返回多个值
```
import math
def move(x,y,step,angle=0):
    nx = x + step * match.cos(angle)
    ny = y - step * match.sin(angle)
    return nx,ny
```

- 递归函数

    在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数

```
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)
```

## 高级特性

- 切片 取一个list 或 tuple 的部分元素是非常常见的操作。

```
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
```

获取前3个元素应该怎么办

    1). 使用笨方式获取

    [L[0], L[1], L[2]]

    2). 使用循环方式获取

    ```
    r = []
    n = 3
    for i in range(n):
        r.append(L[i])

    print(r)
    ```

    3). 使用切片方式获取

    L[0:3]  //  从索引0开始取，直到索引3为止，但不包括索引3。即0，1，2

    L[:3]   //  如果第一个索引是0，可以省略

    L[-1]   //  获取倒数第一个元素

    L[:10:2]    //  前10个数，每两个取一个 [0，2，4，6，8]

    L[::5]  //  每5个取一个

    L[:]    //  复制整个list

- 迭代 如果给定一个 list 或 tuple ，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代

    1). for循环
```
d = {'a':1, 'b':2, 'c':3}
for key in d:
    print(key)
```
    2). 迭代value
```
for value in d.values():
    print(value)
```























































