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