# -*- coding: utf-8 -*-
#Chapter 4
#标准类型： int bool long float complex string list truple #dictory
#None, File Function Module Class

#内部类型：代码，帧，跟踪记录，切片，省略，Xrange
#代码对象 compile() exec eval()
#帧对象 Python的执行栈帧
#跟踪记录 对象
'''
Traceback (innermost last):
File "<stdin>",line N?, in ???
ErrorName: error reason
'''
#异常发生时，一个包含针对异常的栈跟踪信息的跟踪记录对低昂被创建
#切片对象
'''
foostr = 'abcde'
print foostr[::-1]
#[起始索引：结束索引：步进值]
'''

'''
a = [5, 'hat', -9.3]
b = a
print a is b
'''

'''
cmp(obj1,obj2) #比较两个对象
repr(obj)     #返回一个对象的字符串表示
str(obj)    #返回对象适合可读性好的字符串表示
type(obj)    #得到一个对象的类型
'''

'''
print type(4)
a,b = -4,12
print cmp(a,b)
'''

'''
def displayNumType(num):
	print num, 'is',
	if isinstance(num, (int, long , float, complex)):
		print 'a number of type:', type(num).__name__
	else:
		print 'not a number at all!!'

displayNumType(-69)
displayNumType(9999999999999999999999L)
displayNumType(98.6)
displayNumType(-5.2+1.9j)
displayNumType('XXX')
'''

'''
def displayNumType(num):
	print num, 'is',
	if type(num) == type(0):
		print type(0).__name__
	if type(num) == type(0L):
		print type(0L).__name__
	if type(num) == type(0.0):
		print type(0.0).__name__
	if type(num) == type(0+0j):
		print type(0+0j).__name__
	else:
		print 'not a number at all!!'

displayNumType(-69)
displayNumType(9999999999999999999999L)
displayNumType(98.6)
displayNumType(-5.2+1.9j)
displayNumType('XXX')
'''

#基本：python提供的标准或者核心类型
#内建：是由于这些类型是python默认就提供的
#数据：他们勇于一般数据存储
#对象：是数据和功能的默认抽象
#原始：提供的是最底层的粒度数据存储
#类型：数据类型


#直接访问：数字
#顺序访问：字符串、列表、元组
#映射访问：字典
