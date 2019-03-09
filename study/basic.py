import time
info = {"aa":"gao","bb":"ya","age":36}
ban = ["gao","ya",36]
print("%s %d %s"%(ban[0],ban[2],ban[1]))
print("%s %d %s"%(info["aa"],info["age"],info["bb"]))
print(ban[1:])
# id 求对象地址
print("id 3=>",id(3))
#  //整数除法->直接舍弃小数部分 ** 求幂 divmod(13,3) 得到整数和余数
print(13**3)
print(divmod(13,3))
print(314e-2)
# 变量交换很简单
a,b=1,2
a,b=b,a
print(a,b)
# 四舍五入
x=3.56
print(round(x,1))
x+=1
print(x)
# 时间,距离19700101的时间
print(time.time()//(3600*24*365))
# 逻辑运算 not or and
print(True and False)
# 同一运算 判断两个标识符是不是引用同一个对象 is
# ==比较对象值是否相等 ,默认调用对象的__eq__()
# 在文件里运行时,缓存整数范围[-5,任意正整数]
# is 比 ==运行效率高,在比较变量和None时,应该使用is
m=-6
n=-6
print(m==n)
print(m is n)
# python中字符串是不可变的,Python3使用16位Unicode编码
# ord 求编码
print("ord=>",ord('杨'))
print("char=>",chr(5671))
# 定义多行字符串 \ 续行符
resume = '''wedfe\
"dfe"'''
print("resume=>",resume)
# 打印不换行
print("aa",end="**")
print("bb")
# 从控制台读取数据
name = input("请输入名字:")
print("name=>",name)

