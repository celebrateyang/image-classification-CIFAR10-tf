import random
# 统计
# 创建
a = [2,3,'rtt',True]
a.append('ka')
print(a)
b = list('dff,df')
print(b)
c = range(10)
print(type(c))
# 通过range 创建一个整数列表
print(list(range(10)))
print(list(range(2,20,2)))
print(list(range(20,2,-1)))
# 推导生成列表
d = [x*3 for x in range(7)]
print(d)
# if 表示对x进一步过滤
e = [x*2 for x in range(100) if x%9==0]
print(e)
# 增加元素,尽量在列表的尾部添加元素,注意append()方法不返回值,f可以直接用,不可以写成f = f.append(40)
f = [20,30]
f.append(40)
print(f)
# + 不是真正的尾部添加元素,而是创建新的列表对象
print(id(f))
f = f +[50]
print(f,id(f))
# extend
f.extend([100,200])
print(f,id(f))
# insert 尽量避免,因为涉及大量元素拷贝 位移
f.insert(2,7)
print(f)
# 乘法扩展
f = f*3
print(f)
# 删除 ,del 没有返回值,pop 有返回值,默认弹出最后一个元素,remove 删除首次出现的元素
del f[0]
print(f,id(f))
g = f.pop()
print(g)
g = f.pop(1)
print(g,f)
f.remove(40)
print(f)
# 访问和计数
# index 指定元素首次出现位置的索引
h= [10,20,30,40,50,20,60]
print(20,3)
# 统计出现次数
print(h.count(20))
print(20 in h)
print(h[-3])
# 切片操作
print(h[2:4:1])
print(h[::-1])
print(h[-4:-2:1])
# 列表的遍历
for x in h:
    print(x)
# 列表排序,1 原列表内部改动
h.sort()
print(h)
random.shuffle(h)
print(h)
# 2.生成新列表,原列表内部不动
i= sorted(h,reverse=True)
print(i)
# reversed 返回迭代器,从后向前
j= reversed(h)
print(list(j))
print(sum(h),max(h),min(h))
# 二维列表
