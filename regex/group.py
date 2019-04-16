# 用()表示的就是要提取的分组（Group）
import re

m = re.match(r'^(\d{3})-(\d{3,8})$','010-12345')
print(m)

# group(0)永远是原始字符串，group(1)、group(2)……表示第1、2、……个子串。
print(m.group(0))
print(m.group(1))
print(m.group(2))
