# import os
# import time
import datetime

print('Hello World!')
print('Time is ', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S %A'))
print('__name__ value: ', __name__)


def main():
    print('this message is from main function')


#Python作为一门较为灵活的解释型脚本语言，其中定义的main()函数只有当该Python脚本直接作为执行程序时才会执行；
#当该python脚本被作为模块(module)引入(import)时，其中的main()函数将不会被执行。
if __name__ == '__main__':
    main()
    # print(__name__)