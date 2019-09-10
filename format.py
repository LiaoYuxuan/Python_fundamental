radius = 25
area = 3.14 * radius * radius

# 以逗号分隔的数字格式
print("{:,}".format(area))

# 保留小数点后两位
print("{:.2f}".format(area))

# 带符号保留小数点后两位(+不是数字的正负号，输出结果仅取决于数字本身)
print("{:+.2f}".format(area))

# 不带小数(直接舍去后面的部分)
print("{:.0f}".format(area))

# 百分比格式(0代表换算为百分数后的小数位数)
print("{:.0%}".format(0.25))

# 指数记法(科学计数法)
print("{:.2e}".format(1000))

# 对齐与填充
# 1.0表示用来填充的东西，可换成其他符号,不填是默认为空格
# 2.^, <, > 分别是居中、左对齐、右对齐
# 3.d前面的数字表示宽度，若数字本身的宽度超过此数字，则此数字无效果
# 4.填充要求数据类型是整形，不能是浮点数
print("{:0>2d}".format(5))
print("{:x<4d}".format(20))
print("{:>3d}".format(10))

# 进制:b->二进制，d->十进制
print("{:b}".format(11))

# 可以使用大括号 {} 来转义大括号
print("{} 对应的位置是 {{0}}".format("runoob"))

# format 函数可以接受不限个参数，位置可以不按顺序
# 不设置指定位置，按默认顺序
print("{} {}".format("hello", "world"))

# 设置指定位置
print("{0} {1}".format("hello", "world"))

# 设置指定位置
print("{1} {0} {1}".format("hello", "world"))

# 可对format参数进行命名
print("数学：{math}, 英语：{english}".format(math=98, english=100))

# 通过字典设置参数
site = {"math": 98, "english": 100}
print("数学：{math}, 英语：{english}".format(**site))

# 通过列表索引设置参数
my_list = [98, 100]
print("数学：{0[0]}, 英语：{0[1]}".format(my_list))
# "0" 是必须的

# 输出结果
# 1,962.5
# 1962.50
# +1962.50
# 1962
# 25%
# 1.00e+03
# 05
# 20xx
#  10
# 1011
# runoob 对应的位置是 {0}
# hello world
# hello world
# world hello world
# 数学：98, 英语：100
# 数学：98, 英语：100
# 数学：98, 英语：100