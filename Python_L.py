# _*_ coding: utf-8 _*_

'''
s1 = 72
s2 = 85

r =  (s2-s1)/s1*100
print('%.1f%%'%r)
'''

'''
def add_end(L = []):
	L.append('END')
	return L

print (add_end())
print (add_end())
'''

'''
def  add_end(L =None):
	if L is None:
		L = []
	else:
		L.append('END')
	return L
	pass
'''

#可变参数函数
'''
def calc(numbers):
	sum =0
	for n in numbers:
		sum += n*n
	return sum
	pass

isum = calc([1,2,3,4,5])
print(isum)
nums = [1,23,4,5]
iSum_n = calc(*nums)
print(iSum_n)
'''
'''
def person(name, age , **kw):
	print('name',name,'age',age,'other',kw)

person('Bob',35,city = 'Beijing')
extra = {'city':'Beijing', 'job':'Engineer'}
person('Bob',35,**extra)
'''

'''
#*后面被视为命名关键字参数
def person(name, age, *, city, job):
	print(name, age ,city, job)
'''

#*args 是可变参数 tuple  **kw是关键字参数 接受 dict

#递归函数
'''
def fact(n):
	if n= 1:
		return 1
	return n*fact(n-1)
'''

#判断是否可迭代
'''
from collections import Iterable
print (isinstance('abc',Iterable))
'''

'''
from collections import Iterable
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s,Iterable)]
print(L2)
'''

#pratice
'''
def triangles():
	L = [1]
	while  True:
		yield L
		L0 = L[:]
		for i in range(1,len(L0)):
			L[i] = L0[i-1]+L0[i]
		L.append(1)
		pass

k = 0
for t in triangles():
	print(t)
	k += 1
	if k ==10:
		break
'''
'''
import math
def normalize(name):
	return name.lower().capitalize()

L = ['adam', 'LISA', 'barT']
print(list(map(normalize,L)))
'''


'''
#筛选器设计
#1.构建所需要的序列
def _odd_iter():
	n = 1
	while True:
		n += 2
		yield n
		pass
#2.构建筛选器
def _not_divisible(n):
	return lambda x: x%n>0

#3.获得生成器

def primes():
	yield 2
	it = _odd_iter()
	while True:
		n = next(it)
		yield n
		it = filter(_not_divisible(n),it)
		pass

for n in primes():
	if n<1000:
		print(n)
	else:
		break
'''

'''
def is_palindrome(n):
	str_n = str(n)
	if str_n[:] == str_n[-1::-1]:
		return True
	else:
		return False

output = filter(is_palindrome,range(1,1000))
print(list(output))
'''

'''
def by_name(t):
	for s in t:
		if isinstance(s,str):
			return s
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L2 = sorted(L,key=by_name)
print(L2)
'''
'''
import functools

def  log(text = None):
	def decorator(func):
		@functools.wraps(func)
		def  wrapper(*args, **kw):
			print('%s %s():'%(text,func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator

@log()
def now():
	print('2015-3-15')

now()
'''

'''
import functools
def log(func):
	@functools.wraps(func)
	def wrapper(*args,**kw):
		print('begin %s'%func.__name__)
		func(*args,**kw)
		print('end %s'%func.__name__)
		return
	return wrapper

@log

def now():
	print('2015-3-15')
'''



now()

