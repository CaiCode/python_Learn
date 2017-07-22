'''
from operator import add, sub
from random import randint, choice

ops = {'+':add, '-': sub}
MAXTRIES = 2

def doprob():
	op = choice('+-')
	nums = [randint(1,10) for i in range(2)]
	nums.sort(reverse = True)
	ans = ops[op](*nums)
	pr = '%d %s %d = ' %(nums[0], op, nums[1])
	oops = 0
	while True:
		try:
			if int(raw_input(pr)) == ans:
				print 'correct'
				break
			if oops == MAXTRIES:
				print 'answers\%s%d'%(pr, ans)
			else:
				print 'incorrect.. try again'
				oops += 1
		except(KeyboardInterrupt,EOFError,ValueError):
			print 'invalid input ... try again'

def main():
	while  True:
		doprob()
		try:
			opt = raw_input('again?[y]').lower()
		if opt and opt[0] == 'n':
			break
		except(KeyboardInterrupt, EOFError):
			break
		pass


if __name__ == '__main__':
	main()
'''

#python是先对函数进行声明后然后再进行调用
'''

def foo():
	print ('in foo()')
	bar()

def bar():
	print ('in bar()')

print (foo())
'''

#内嵌函数
'''
def foo():
	def  bar():
		print('bar() called')
	print ('foo() called')
	bar()

print (foo())
'''
#函数（与方法）装饰器
'''
装饰器的语法以@开头接着是装饰器函数的名字和可选的参数。、
紧跟着装饰器声明的是被修饰的函数，和装饰函数的可选参数
'''
'''
@decorator(dec_opt_args)
def func2Bdecorated(func_opt_args):
'''

'''
class MyClass(object):
	def  staticFoo():
		staticFoo = staticmethod(staticFoo)

class MyClass(object):
	@staticmethod
	def  staticFoo():
'''

'''
@deco2
@deco1
def func(arg1, arg2,...):pass

#等价于
def func(arg1, arg2,...):pass
func = deco2(deco1(func))
'''

#无参数
'''
@deco1
def foo(): pass

foo = deco(foo)
'''

#有参数
'''
@decomaker(deco_args)
def foo():
	pass

foo = decomaker(deco_args)(foo)
'''


#什么是装饰器
'''
装饰器实际就是函数，接受函数对象
1.引入日志
2.增加计时逻辑来监测性能
3.给函数加入事务的能力
'''

'''
from time import ctime, sleep
def  tsfunc(func):
	def  wrappedFunc():
		print('[%s]%s() called'%(ctime(), func.__name__))
		return func()
	return wrappedFunc


@tsfunc
def foo():
	pass

foo()
sleep(4)

for i in range(2):
	sleep(1)
	foo()
'''


#传递函数

'''
def convert(func, seq):
	'conv. sequence of numbers to same type'
	return [func(eachNum) for eachNum in seq]

myseq = (123,45.67, -6.2e8, 999999999L)
print (convert(int, myseq))
print (convert(long, myseq))
print (convert(float, myseq))
'''

#形式参数
'''
由在调用时要传入函数的所有参数组成
1.位置参数：以在被调用函数中定义的准确顺序来传递
2.默认参数：给参数提供预先定义的默认值
'''
#可变长度的参数
#非关键字可变长参数（元组）

'''
def function_name([formal_args,]*vargs_tuple):
	"function_documentation_string"
	function_body_suite
'''
#星号操作符之后的形参将作为元组传递给函数
#元组保存了所有传递给函数的“额外”的参数
'''
def tupleVarArgs(ars1, arg2 = 'defaultB',*theRest):
	print ('formal arg 1:') 
	print(ars1) 
	print('formal arg2:') 
	for eachXtrArg in theRest:
		print('another arg:') 
		print(eachXtrArg)


tupleVarArgs('abc')
tupleVarArgs('abc','123')
'''

#关键字变量参数
'''
存在不定数目的或者额外集合的关键字的情况中
参数被放入一个字典中，字典中键为参数名，值为相应的参数值
'''

'''
def dictVarArgs(arg1, arg2='defalutB', **theRest)
'''

#调用带有可变长参数对象函数

#函数式编程y:

'''
def testit(func, *nkargs, **kwargs):
	try:
		retval = func(*nkargs, **kwargs)
		result = (True, retval)
	except Exception, diah:
		result = (False,retval)
	return result

def  test():
	funcs = (int , long ,float)
	vals = (1234, 12.34, '1234','12.34')
	for  eachFunc in funcs:
		print('-'*20)
	for  eachVal in vals:
		retval = testit(eachFunc,eachVal)
	if retval[0]:
		print('%s(%s) = '%(eachFunc.__name__,'eachVal'),retval[1])
	else:
		print('%s(%s) = FAILED'% (eachFunc.__name__,'eachVal'),retval[1])

if __name__ == '__main__':
	test()
'''

#函数式编程
#匿名函数与lambda
'''
python 允许用lambda关键字创造匿名函数
lamba[arg1[,arg,...argN]:expression
'''

'''
def add(x,y):return x+y? lamba x,y:x+y
'''

'''
内建函数                      描述
apply(func[, nkw][,kw])       用可选参数来调用func, nkw 为非关键字参数,kw 关键字参数
filter(func, seq)             调用一个布尔函数func来迭代遍历每个seq中的元素，返回序列
map(func, seq1[,seq2...])     将函数func作用于给定序列的每个元素，并用一个列表来提供返回值
reduce(func,seq[, init])      将二元函数作用于seq序列的元素，每次携带一对
'''

#偏函数应用
'''
currying的概念将函数式编程的概念和默认参数以及可变参数结合在一起。一个带n个参数
curried的函数固化第一个参数为固定参数，并返回另一个带n-1歌参数函数对象
'''

'''
from operator import add,mul
from functools import partial
add1 = partial(add,1)
baseTwo = partial(int, base=2)
baseTwo.__doc__ = 'Convert base 2 string to an int'
'''

'''
from functools import partial
import Tkinter

root = Tkinter.Tk()
MyButton = partial(Tkinter.Button, root, fg = 'white', bg = 'blue')
b1 = MyButton(text = 'Button 1')
b2 = MyButton(text = 'Button 2')
qb = MyButton(text = 'QUIT', bg = 'red', command = root.quit)
b1.pack()
b2.pack()
qb.pack(fill = Tkinter.X, expand=True)
root.title('PFAs!')
root.mainloop()
'''

'''
核心笔记：搜索标识符
当搜索一个标识符时候，先从局部作用域开始搜索。如果在局部作用域
内没有找到这个名字，一定会在全局域内找到这个变量
'''

#闭包
#追踪闭包变量
'''
output = '<int %r id = %#0x val = %d>'
w = x = y = z =1


def  f1():
	x = y = z = 2

def f2():
	y = z = 3
	pass

def f3():
	z = 4

print (output %('w', id(w),w))
print (output %('x', id(x),x))
print (output %('y', id(y),y))
print (output %('z', id(z),z))

clo = f3.func_closure
if clo:
	print("f3 closure vars:", [str(c)for c in clo])
else:
	prin("no f3 closure vars")
'''

j,k = 1,2

def proc1():
	j,k = 3,4
	print("j == %d and k == %d"%(j,k))
	k = 5
	def proc2():
		j = 6
		proc1()
		print("j == %d and k == %d"%(j,k))

		k = 7
		proc1()
		print("j == %d and k == %d"%(j,k))

		j = 8
		proc2()
		print("j == %d and k == %d"%(j,k))

proc1()


