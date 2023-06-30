m = ['+', '-', '*', '/']
print('你好，这是一个科学计算器')
print('制作人：吴优')
a = int(input('请输入第一个需要运算的数字：'))
m = input('请输入运算法则，+代表加法，-代表减法，*代表乘法，/代表除法：')
b = int(input('请输入第二个需要运算的数字：'))
if m == '+':
    n = a + b
    print('答案是：',str(n))
elif m == '-':
    n = a - b
    print('答案是：',str(n))
elif m == '*':
    n = a * b
    print('答案是：',str(n))
elif m == '/':
    n = a / b
    print('答案是：',str(n))
else:
    print('你的输入结果有误！')

input('按任意键退出')