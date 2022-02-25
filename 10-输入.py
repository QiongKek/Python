"""
在 python 中，程序接受用户输入的数据的功能既是输入
输入的语法：
    input("提示信息")

输入特点：
    当程序执行到input，等待用户输入，输入完成之后才继续向下执行
    在python中，input接收用户输入后，一般存储到变量，方便使用
    在python中，input会把接收到的任意用户输入的数据都当做字符串处理


"""

password = input('请输入您的密码：')
print(f'您输入的密码是{password}')
print(type(password))

