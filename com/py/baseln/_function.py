# def add():
#     print("add")
# add()

# def add(a,b):
#     print(a+b)
# add(1,2)

#注意，python函数没有重载,重名的函数，后面会覆盖前面
# def add(a=100,b=200):
#     print(a+b)
# add()

# def add(a=200,b=100):
#     print(a)
#     print(b)
# add(b=1,a=2)

#不定长参数
#*args表示元组
#**kwargs表示字典
# def fun(a,b,*args,**kwargs):
#     print("a=",a)
#     print("b=",b)
#     print("*args=",args)
#     print("**kwargs=",kwargs)
#     for k,v in kwargs.items():
#         print(k,v)
# fun(1,2,3,3,23,2,3,x=1,y=2)

# list=[1,2,3]
# list+=list
# print(list)

# a=1
# def fun(a):
#     a+=a
#     print(a)
# fun(a)
# print(a)

# b=[1,2]
# def fun(b):
#     b+=b
#     print(b)
# fun(b)
# print(b)

# def fun(a,b):
#     return a+b
# print(1+3)

#带返回值的函数，可以返回多个返回值
# def fun(a,b):
#     return a+b,a-b
# print(fun(1,1))
# a,b=fun(1,1)
# print(a,b)

#方法外是全局变量，方法内是局部变量
#加上global可以改变值，不能在global前定义同名的局部变量
# count=100
# def fun():
#     global count
#     count=20
#     print(count)
# print(count)
# fun()
# print(count)

#递归函数
# def getNum(a):
#     if(a<=2):
#         return 1
#     else:
#         return getNum(a-1)+getNum(a-2)
# for i in range(1,11):
#     print(getNum(i),end="\t")

#匿名函数
# sum=lambda a,b:a+b
# print(type(sum))
# print(sum(1,2))
# def fun(a,b,opt):
#     print(a)
#     print(b)
#     print(opt(a,b))
#     print("----")
# fun(1,2,lambda a,b:a+b)
# fun(1,2,lambda a,b:a-b)
# fun(1,2,lambda a,b:a*b)
# dict=[{"age":17},{"age":27},{"age":19}]
# dict.sort(key=lambda x:x["age"])
# print(dict)


###########自定义函数###########
def add(a,b):
    return a+b
def sub(a,b):
    return a-b




