class Person:
    name="name prop"
    def __init__(self,name,age):
        self.__sex=name
        self.name=name
        self.age=age
    def __new__(cls,name,age):
        return object.__new__(cls);
    def run(self):
        print("method")
    def __str__(self):
        return "hahha"
    def __del__(self):
        print("del...")
    # 私有属性和方法不会被子类继承，也不能被访问
    def __getSex(self):
        print(self.__sex)
    # 一般情况下，私有的属性和方法都是不对外公布的，往往用来做内部的事情，起到安全的作用
    def printSex(self):
        self.__getSex()
# p=Person("hyx",29)
# print(p.name)
# p.run()
# print(p.age)
# print("hahaha")
# p.printSex()

class Animal(object):
    def __init__(self,name):
        self.name=name
    def run(self):
        print(self.name+" is running")

class Active(object):
    def active(self):
        print("active...")

class Cat(Animal,Active):
    def __init__(self,name,type):
        super().__init__(name)
        self.type=type

# cat = Cat("lele", "cat")
# cat.run()
# cat.active()

# “鸭子类型”（和多态还是有区别）
class F1(object):
    def show(self):
        print("F1 show")
class S1(F1):
    def show(self):
        print("S1 show")
class S2(F1):
    def show(self):
        print("S2 show")
class S3:
    def show(self):
        print("S3 show")
def Func(obj):
    obj.show()
# Func(F1())
# Func(S1())
# Func(S2())
# Func(S3())

class Student(object):
    name="zhangsan"
    __age=30
    def __init__(self,name,age):
        self.name=name
        self.__age=age
    def getAge(self):
        return self.__age
    @staticmethod
    def getStaticAge():
        return Student.__age
    @classmethod
    def getClassAge(cls):
        return cls.__age
# print(Student.name)
# print(Student.getStaticAge())
# s=Student("list",100)
# Student.name="changename"
# print(s.name)
# print(s.getAge())
# print(Student.name)
# print(Student.getStaticAge())
# print(Student.getClassAge())

#单例模式
class Singleton:
    __instance=None
    __First_init=True

    def __init__(self,name):
        if self.__First_init:
            self.__First_init=False
            self.name=name
            print("init...")

    def __new__(cls, name):
        print("new")
        if not cls.__instance:
            cls.__instance=object.__new__(cls)
        return cls.__instance

    def run(self):
        print("running...")

# s=Singleton("zhuangsan")
# s1=Singleton("lisi")
# print(id(s))
# print(id(s1))
# print(s.name)
# print(s1.name)

# try:
#     print("test1")
#     print(1/0)
#     open("123.txt","r")
#     print("test2")
# except (FileNotFoundError,ZeroDivisionError) as msg:
#     print("发生异常了")
#     print(msg)
# # except ZeroDivisionError as msg:
# #     print("发生0除异常了")
# #     print(msg)
# else:
#     print("没有异常了")
# finally:
#     print("finally...")
# print("test3")

# class ShortInputError(Exception):
#     def __init__(self,length,atleast):
#         self.length=length
#         self.atleast=atleast
# def func():
#     str=input("请输入参数")
#     try:
#         if len(str)<3:
#             raise ShortInputError(len(str),5)
#     except ShortInputError as msg:
#         print("字符串的长度是%d，至少需要长度是:%d"%(msg.length,msg.atleast))
#     finally:
#         print("执行完毕")
# func()

