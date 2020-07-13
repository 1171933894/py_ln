# coding=UTF-8

# 简单打印文字
'''
print("hello world")
'''

# 获取控制台输入（py3中没有raw_input，只有input，但功能相同）
'''
a=raw_input("请输入字符串")
print(a)
'''

# #除（3）
# print(10/3)
# #整除（3）
# print(10//3.0)
# #乘
# print(10*2)
# #平方
# print(10**2)
#
# a,b=1,2
# print(a)
# print(b)

# age = 20
# if (age < 20):
#     print("小孩")
# elif (age < 40):
#     print("中年")
# else:
#     print("老年")


# i=0
# sum=0
# while i<=100:
#     sum+=i
#     i+=1
# print(sum)

# for i in 1,2,3:
#     print(i)

# for i in range(1,10):
#     print(i)

# for 的 range 函数都是左闭右开区间
# for i in range(1,10):
#     print(i)

# for i in "abc","edf", "adsf", "asdf":
#     print(i)
# else:
#     print("for over")

# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%d*%d=%d"%(j,i,j*i),end="\t")
#         if(j==i):
#             print()

# str = "abcdef"
# print(str[2])
# print(str[-1])
# print(str[-2])

# 切分字符串
# a="abcdef"
# print(a[:3])
# print(a[::2])
# print(a[1:5:2])
# print(a[::-2])
# print(a[5:1:-2])
# print(a[1:5:2])

# mystr = ' hello world and bjsxt yunshuxueyuan sxt beijing '
# print(mystr.index("sxt"))
# print(mystr.rindex("sxt"))
# print(mystr.find("sxt1"))
# print(mystr.count("sxt",0,40))
# print(mystr.split(" "))
# print(mystr.split(" ",3))
# print(mystr.capitalize())
# print(mystr.upper())
# print(mystr.title())
# print(mystr.ljust(100,"*"))
# print(mystr.rjust(100,"*"))
# print(mystr)
# print(mystr.strip())
# print(mystr.partition("sxt"))
# print(mystr.rpartition("sxt"))
# print("abcdef".isalpha())
# print("1234".isdigit())
# print("abd23".isalnum())
# print(" ".isspace())

# list=["abcd",123,True,123.456]
# list2=['a',"b","c"]
# list3=['a',["b","c"]]
# print(list[2])
# print(list[::-1])
# for i in list:
#     print(i)
# for i,v in enumerate(list):
#     print(i,v)
# list.append("append")
# list.insert(0,"first")
# list.extend(list2)
# list.extend(list3)
# print(list)
# list[0]='second'
# print(list)
# print(list.index(123,0,3))
# print(list.count("abcd"))
#
# print(list)
# list.remove('abcd')

# print(list)
# list.pop(0)
# print(list)
# del list
# print(list)

# list2=[5,4,3,2,1]
# # sort 函数必须要求list为同类型
# # list2.sort(reverse=False)
# print(list2)
# list2.reverse()
# print(list2)

#元组通过()来标识，元素中的元祖是不可变的
# tuple=(1,"abc",True,1.123)
# print(tuple)
# print(tuple[2])
# t=(1)
# print(t)
# print(type(t))
# t2=(1,)
# print(t2)

# dict={"a":100,"b":200,"c":300}
# print(dict)
# print(dict["a"])
# print(dict.get("b"))
# dict["d"]=400
# dict["e"]=None
# print(dict)
# print(type(dict))
# dict1={1,2,3,4}
# print(type(dict1))
#
# set = set([1,2,3,4])
# print(type(set))
# print(set)
#
# print(len(dict))
# print(dict.keys())
# print(dict.values())
# print(dict.items())
#
# for i in dict.keys():
#     print(i,dict[i])
#
# for v in dict.values():
#     print(v)
#
# for i,v in dict.items():
#     print(i,v)
#
# print(set)
# set.add(7)
# print(set)
# print(type(set))

#f=open("C:\\Users\\heyuanxin3\\Desktop\\test123.txt","w")
# f.write("abc")
# f.close()

# f=open("C:\\Users\\heyuanxin3\\Desktop\\test123.txt","r")
# print(f.read())
# print(f.readline())
# print(f.readlines())
# for i in f.readlines():
#     print(i)
# f.close()

# import keyword
# print(keyword.kwlist)

# import os
# print(os.name)
# print(os.listdir())
# print(os.getcwd())
# os.remove("C:\\Users\\heyuanxin3\\Desktop\\test123.txt")
# os.mkdir("C:\\Users\\heyuanxin3\\Desktop\\testabc")
# print(os.path.isdir("C:\\Users\\heyuanxin3\\Desktop\\testabc"))