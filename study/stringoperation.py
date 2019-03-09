import io
# python 里面字符串一旦定义,则是不可改变的.
# str转字符串
print(str(5.12e2))
# 字符串正向偏移量是从0开始,反向偏移量从-1开始
a='abcdefghijklmnopqrstuvwxyz'
print(a[25])
print(a[-26])
b = a.replace('c','高')
print(a)
print(b)
a= a.replace('c','哈')
print(a)
# 字符串切片操作
# 第一到第5,包头不包尾
print(a[1:5])
# 2表示步长为2
print(a[1:5:2])
# [:]取整个字符串,[2:]从2开始,直到最后,[:5]从起始到最后,[-8:-3]
# [::-1]步长为负1,反向提取
print(a[::-1])
# 字符串切割与合并.split 自动分割成列表,join()连接和+差不多,join()性能好,
# +会生成新的对象
x = "to be or not to be"
print(x.split())
print(x.split('to'))
liebiao = ['bam','oo','yang']
print(''.join(liebiao))
# format()
bb ='名字是{0},年龄是{1}'
bb= bb.format('kk',11)
print(bb)
cc = '名字是{name},年龄是{age}'
print(cc.format(name='dd',age=32))
# 填充与对齐 ...
#  数字格式化 冒号表示后面需要按指定格式填充
a='我有存款{0:.2f}'
print(a.format(345.56789))
# 可变字符串,当字符串需要大量修改时,考虑使用
astring = 'hello,bamboo'
changestring = io.StringIO(astring)
changestring.seek(4)
changestring.write('haha')
print(changestring.getvalue())
# 比较运算符 可以连用
m=4
print(1<m<10)
# 乘法操作,实现复制
mul = 'gua'
print(mul*3)
mul1 = [3,4,5]
print(mul1*3)

