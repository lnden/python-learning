# 获取当前日期和时间
from datetime import datetime
now = datetime.now()
print(now)


print('--------------------分割线------------------------')

# 获取指定日期和时间
dt = datetime(2015,4,19,12,20)
print(dt)


print('--------------------分割线------------------------')
# datatime类型转换为timestamp
dd = datetime(2015,4,19,12,20)
ds = dd.timestamp()
print(ds)


print('--------------------分割线------------------------')
# timestamp也可以直接被转换到UTC标准时区的时间

t = 1429417200.0
# 本地时间
print(datetime.fromtimestamp(t))
# UTC时间
print(datetime.utcfromtimestamp(t))


print('--------------------分割线------------------------')
# str转换为datetime
cday = datetime.strptime('2015-6-1 18:19:59','%Y-%m-%d %H:%M:%S')
print(cday)


print('--------------------分割线------------------------')
# datetime转换为str
nows = datetime.now()
print(nows.strftime('%a,%b %d %H:%M'))


print('--------------------分割线------------------------')
# datetime加减
from datetime import timedelta
nowe = datetime.now()
print(nowe)
add = nowe + timedelta(hours = 10)
print(add)
subtract =nowe - timedelta(days=1)
print(subtract)
more = nowe + timedelta(days=2,hours=12)
print(more)
