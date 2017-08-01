#! /usr/bin/env python3 #增加这行可以直接terminal执行.py文件
# 基础语法
identifier = 4
if identifier == 1:
    import keyword

    print(keyword.kwlist)
    print("hello world")
    # end='' 表示输出不换行
    print("nihao"'j''k', end="");
    number = input("请输入\n")  # 多行statement用（分号后加空格的形式来连接）
    if number == "a":
        print(number + ' world')
    else:
        # 多行文本直接用 '''开始和'''结束或者（"""），两者通用
        print('''error
        啊； ；啊''')
    import sys

    for i in sys.argv:
        print(i)
    print('sys.path:', sys.path)
elif identifier == 2:
    # 同时多个变量赋值。整数、浮点数、布尔型、复数型、字符串型
    a, b, c, d, e = 10, 1.2, True, 1 + 2j, 'hello'
    # type获取变量的类型
    print(type(a), type(b), type(c), type(d), type(e))
    # 是否某个类型的变量
    print(isinstance(a, int))
    # 是否某个类的子类
    print(issubclass(type(e), str))
    # 删除对象的引用
    del a, b
    p1 = 2 / 4  # 结果为浮点数 0.5
    p2 = 2 // 4  # 结果为整数 0
    p3 = 2 ** 5  # 乘方 结果为 2^5 = 32

    # String 字符串
    print('-----------String-----------')
    tempStr = 'hello_world'
    print(tempStr)
    print(len(tempStr))
    # 字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。
    print(tempStr[1:3])  # 输出字符串截取，1，3表示从第2个到第4个index，可以0，-3表示从第一个到最后第四个
    print(tempStr[2:])  # 表示从第三个到最后
    print(tempStr * 2)  # 表示字符串复制一次，追加到后面
    print(tempStr + "test")  # 字符串拼接
    # tempStr[1] = 2 #不能修改字符串中的某一字符
    print('he\nllo')
    print(r'he\nllo')  # 用在字符串前面加r或者R表示输出原始字符串，不转义
    # \表示下一行续上上一行，用于段落
    print('hello' \
          'world')
    # 多行string也可用用（'''stringContent'''） 形式或者（"""stringContent"""）来表达
    print('''
    'hello'
    'test'
    ''')
    word = "hello"
    print(word.capitalize())#将第一个字符大写
    print(word.count('l', 0, 4))
    print(word[2])  # 表示取word中index为2的字符
    #字符串格式化
    print('我叫%s,age：%d' %('python', 10))

    # List 列表
    print('-----------List-----------')
    list1 = ['啊', 2, c, e]
    list2 = ['wo', c]
    # 具体的语法同String
    print(list1 + list2)  # 列表的相加，整合成一个列表
    print(list2 * 2)  # 列表的复制一份追加在列表后
    print(list1[0:3])
    print(list1[0:-3])
    # 列表中的元素改变
    del list1[0]#删除一个元素
    list1.remove(2)
    list1[0] = '哦'
    list1[1:3] = [3, 4]
    print(list1)
    list1[0:2] = []  # 列表中批量连续元素的删除
    print(list1)
    list1[0:1] = []  # 列表中单个元素删除
    print(list1)
    list1.append(e)
    print(list1)

    # Tuple 元组 #具体的语法和string一样，不能修改元组中的某一元素
    print('-----------Tuple-----------')
    tuple1 = ('tuple', e, 2.3, 5)
    print(tuple1)
    print(tuple1[0])
    print(tuple1[2:3])
    print(tuple1 * 2)
    tuple2 = ('tuple2', [1, 2], 3)
    print(tuple2)
    print(3 in tuple2)

    # Set 集合，无序不重复集合
    print('-----------Set-----------')
    student1 = {'A', 'B', 'C', 'D', 'E'}
    student2 = set('abcde')  # student1和student2两种集合创建方式一样
    print(student2)
    if 'a' in student2:
        print('A is a student')
    else:
        print('A is\'t a student')
    set1 = set('abcd123456')
    set2 = {'a', 'b', 'c', 'd', '1', '2', '3', '10', 'a'} #重复的元素自动被合并
    print(set1 - set2) #两个集合的差集
    print(set1 & set2) #两个集合的交集
    print(set1 | set2) #两个集合的并集
    print(set1 ^ set2) #两个集合中不同时存在的元素（交集取反）
    #Dictionary 字典
    print('-----------Dictionary-----------')
    dic1 = {}
    dic1['name'] = 'hello'
    dic1[2] = 'age'
    dic2 = {'name': 'hello', 'age': 18}
    print(dic1)
    print(dic2)
    print(dic2.keys())
    print(dic2.values())
    dic3 = dict([(1, 'a'), (2, 'b'), (3, 'c')])#dict的构造函数
    print(dic3)
    dic4 = dict(ab=1, cd=2, Taobao='taobao')
    print(dic4)
    dic4.clear()#清空字典
    print(len(dic3.keys()))
    print({x: x**2 for x in (2, 4, 6)}) #快速构建一个有规律的字典key：key**2
    for x in dic3:
        print(str(x)+':'+str(dic3[x]))

    print('-----------运算符-----------')
    a = True
    b = False
    if a and b:
        print(a, b)
    if a or b:
        print(a, b)
    if not(a and b):
        print(a, b)
    if a in dic3:
        print(a)
    if a not in dic3:
        print(b)
    if a is b:
        print('a is b')
    if a is not b:
        print('a is not b')
    if id(a) == id(b): #等同于 a is b
        print('a is b')
elif identifier == 3:
    for i in range(3, 9, 2): #第一个为起点数、第二个为<9 、第三个为步长
        print(i)
    guess = -1
    number = 9
    while guess != number:
        guess = int(input('请输入一个数字\n'))
        if guess < number:
            print('太小了')
        elif guess > number:
            print('太大了')
        else:
            print('猜对了')

elif identifier == 4:
    def fibonacci(n):
        a, b, counter = 0, 1, 0
        while True:
            if counter > n:
                return
            yield a
            a, b = b, a+b
            counter += 1
    f = fibonacci(10)
    for i in iter(f):
        print(i)
    def averageNumber(x, y):
        return (x+y)/2
    print(averageNumber(2, 3))
    def appendList(tempList):
        return tempList.append([1, 2])
    tempList1 = [0,1.5]
    appendList(tempList1)
    print(tempList1)










else:
    print('finished')

# 基本数据类型
