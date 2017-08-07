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

'''
import functools
int2 = functools.partial(int ,base=2)
'''

#模块
'''
from PIL import Image
im = Image.open('test.png')
print(im.format, im.size, im.mode)
im.thumbnail((200,100))
im.save('thumb.png','PNG')
'''

'''
class Student(object):
	def __init__(self, name ,score):
		self.name = name
		self.score = score
		pass

	def  print_score(self):
		print('%s:%s'%(self.name, self.score))
		pass

	def  Get_Grad_rank(self):
		if self.score >= 90:
			return 'A'
		elif self.score >= 60:
			return 'B'
		else:
			return 'C'

bart = Student('Bart Simpson',59)
bart.print_score()
'''

'''
class Animal(Object):
	def run(self):
		print('Animal is running')
		pass

class Dog(Animal):
	def  run(self):
		print('Dog is running')
		pass

class Cat(Animal):
	def run():
		print('Cat is running')
		pass
'''

'''
class MyObject(object):
	def __init__(self):
		self.x = 9
	def power(self):
		return self.x*self.x

obj = MyObject()
hasattr(obj,'x')
setattr(obj,'y',19)
getattr(obj,'y')
'''


'''
def readImage(fp):
	if hasattr(fp,'read'):
		return readData(fp)
	return None
'''


'''
#实例属性和类属性
class Student(object):
	def __init__(self,name):
		self.name = name

#此处的name为实例属性

class Student(object):
	name = 'Student'

#此处为类属性
'''

'''
class Student(object):
	pass

#绑定属性
s = Student()
s.name = 'Michael'

#绑定方法(实例)
def set_age(self,age):
	self.age = age
from types import MethodType
s.set_age = MethodType(set_age,s)

#绑定方法(class)
def set_score(self,score):
	self.score

Student set_score = set_score
#限制实例添加的属性数量

class Student(object):
	__slots__ = ('name','age')
'''


'''
class Screen(object):
	@property
	def width(self):
		return self._width

	@width.setter
	def width(self,value):
		if not isinstance(value,int):
			raise ValueError("must be integer")
		if value < 0:
			raise ValueError("must > 0")
		self._width = value

	@property
	def height(self):
		return self._width

	@height.setter
	def height(self,value):
		if not isinstance(value,int):
			raise ValueError("must be integer")
		if value < 0:
			raise ValueError("must > 0")
		self._height = value

	@property
	def  resolution(self):
		return self._height*self._width
		pass


s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution
'''

'''
#多重继承

class Animal(object):
	pass

#大类
class Mammal(Animal):
	pass

class Bird(Animal):
	pass

#各种动物
class Dog(Mammal):
	pass

class Bat(Mammal):
	pass

class Parrot(Bird):
	pass

class Ostrich(Bird):
	pass

class Runnable(object):
	def  run(self):
		print("running...")
		pass

class Flyable(object):
	def fly(self):
		print("Flying...")

class Dog(Mammal,Runnable):
	pass

class Bat(Mammal,Flyable):
	pass
'''

'''
class Student(object):
	def  __init__(self,name):
		self.name = name
		pass
#负责打印的字符串
	def __str__(self):
		return 'Student object (name: %s)' %self.name

#直接显示变量调用的不是__str__()而是__repr__()返回的是程序开发者看到的字符串
s = Student('Michael')
print(s)
'''
#__iter__()返回迭代对象
#__next__()得到下一个值

'''
class Fib(object):
	def __init__(self):
		self.a, self.b = 0 ,1
		pass

	def __iter__(self):
		return self
		pass

	def  __next__(self):
		self.a, self.b = self.b, self.a + self.b
		if self.a > 10000:
			raise StopIteration()
		return self.a
		pass

	def __getitem__(self,n):
		if isinstance(n ,int):
			a,b = 1,1
			for x in range(n):
				a,b = b, a+b
			return a
		if isinstance(n, slice):
			start = n.start
			stop = n.stop
			if start is None:
				start = 0
			a,b = 1, 1
			L= []
			for x in range(stop):
				if x >= start:
					L.append(a)
				a,b = b, a+b
			return L
for n in Fib():
	print(n)
f = Fib()
print (f[2])
print(f[:5])

#__getitem__()获得元素

class Student(object):
	#当没有这个属性的时候 动态返回一个属性或者函数
	def  __getattr__(self,attr):
		if attr == 'score':
			return 99
'''

'''
class Chain(object):

	def __init__(self, path = 'GET'):
		self._path = path

	def __getattr__(self,path):
		return Chain('%s(%s)'%(self._path, path))

	def __call__(self,attr):
		return Chain('%s(%s)'%(self._path, attr))

	def __str__(self):
		return self._path

	def GetPath(self):
		return self._path

	__repr__ = __str__

chain = Chain().users('michael').repos
path = chain.GetPath()
print(path)
'''

'''
from enum import Enum,unique

Month = Enum('Month',('Jan','Feb','Mar'))
for name, member in Month.__members__.items():
	print(name, '=>', member, ',', member.value)

@unique
class Weekday(Enum):
	Sun = 0
	Mon = 1
	Tue = 2
	Wed = 3
	Thu = 4
	Fri = 5
	Sat = 6

for name, member in Weekday.__members__.items():
	print(name, '=>' ,member,',',member.value)
'''

'''
#使用元类
def fn(self, name = 'world'):
	print('Hello, %s' %name)

#创建Hello class
#1.class的名称 2.继承的父类集合3.与函数绑定
Hello = type('Hello',(object,),dict(hello = fn))
'''
#metaclass -> create Class -> create example

'''
class ListMetaclass(type):
	def __new__(cls, name, bases, attrs):
		attrs['add'] = lambda self, value: self.append(value)
		return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass = ListMetaclass):
	pass

L = MyList()
L.add(1)
print(L)
'''

#ORM框架 对象—关系映射

#Field Class

'''
class Field(oject):
	def __init__(self, name, column_type):
		self.name = name
		self.column_type = column_type

	def __str__(self):
		return '<%s,%s>' %(self.__class__.__name__,self.name)

class StringField(Field):

	def __init__(self, name):
		super(StringField.self).__init__(name,'varchar(100)')


class IntegerField(Field):
	def __init__(self,name):
		super(IntegerField,self).__init__(name,'bigint')

class ModelMetaclass(type):

	def __new__(cls, name, bases, attrs):
		if name = 'Model':
			return type.__new__(cls,name,bases,attrs)
		print('Found model: %s' %name)
		mappings = dict()
		for k,v in attrs.items():
			if isinstance(v, Field):
				print('Found mapping: %s ==> %s' %(k,v))
				mappings[k] = v
		for k in mappings.keys():
			attrs.pop(k)
		attrs['__mappings__'] = mappings
		attrs['__table__'] = name
		return type.__new__(cls, name, bases, attrs)

class Model(dict, metaclass = ModelMetaclass):

	def __init__(self, **kw):
		super(Model,self).__init__(**kw)

	def __getattr__(self, key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Model' object has no attribute '%s'"%key)

	def __setattr__(self,key ,value):
		self[key] = value

	def save(self):
		fields = []
		params = []
		args = []
		for k,v in self.__mappings__.items():
			fields.append(v.name)
			params.append('?')
			args.append(getattr(self,k,None))
		sql = 'insert into %s (%s) values (%s)' %(self.__table__,','.join(fields),','.join(params))
		print('SQL:%s' %sql)
		print('ARGS:%s' %str(args))
'''




