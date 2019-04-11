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





































