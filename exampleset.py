# 斐波那契数列生成 P19
# a, b = 0, 1
# while a < 1000:
#     print(a, end=',')
#     a, b = b, a + b

# 日期和时间的输出 P21
from datetime import datetime
now = datetime.now()
print(now)
print(now.strftime("%x"))  # 输出其中的日期部分
print(now.strftime("%X"))  # 输出其中的时间部分

