# _*_ coding: utf-8 _*_
'''
s = 'abcde'
for i in [None] + range(-1,-len(s),-1):
	print s[:i]
'''

'''
list(iter)  把可迭代对象转换为列表
str(obj)    把obj对象转换成字符串
unicode(obj)把对象转换成Unicode 字符串
basestring() 为str何unicode 函数提供父类
tuple(iter)   把一个可迭代对象转换成一个元组对象
'''

'''
enumerate(iter)  接受一个可迭代对象最为参数返回一个enumerate
                 对象，由iter每个元素的index和item值组成的元组
len(seq)         返回长度
max(iter, key = None) or
max(arg0,arg1....,key = None) 返回最大值，其中key必须是一个
                    可以传给sort方法的，用于比较的回调函数
min(iter, key = None) or
min(arg0,arg1....,key = None)
reversed(seq) 接受一个序列作为参数，返回一个逆序访问的迭代器
sorted(iter
func = None,
key = None,
reverse = False) 接受一个可迭代对象作为参数，返回一个有序的列表
sum(seq, init =0) 返回seq 和可选参数init的总和相当于
reduce(operator.add, seq,init)
zip([it0,it1....itN])返回一个列表，第一个元素是it0,it1...
这些元素的第一个元素组成的一个元组
'''

"""
import string

alphas = string.letters + '_'
nums = string.digits

print 'Welcome to the Identifier Checker v1.0'
print 'Testees must be at least 2 chars long'
myInput = raw_input('Identifier to test?')

count = 0;
if len(myInput) > 1:
	if myInput[0] not in alphas:
		print ''' invalid: first symbol mus be
		alphabetic'''
	else:
		count += 1
		for otherChar in myInput[1:]:
			if otherChar not in alphas + nums:
				print ''' invalid: remaining 
				symbols must be alphanumeric'''
				break
			else:
				count += 1
		if count == len(myInput):
			print 'OK'
"""

'''
s = ' '.join(('Spanish', 'Inquisition', 'Made Easy'))
print s
print ('%s%s' % (s[:3], s[20])).upper()
'''

'''
格式化操作符辅助指令

*          定义宽度或者小数点精度
-          用做左对齐
+          在正数前面显示加号
<sp>       在整数面前显示空格
#          显示进制
0          显示的数字前面填充‘0’
%          
(var)      映射变量
m.n        m是显示的最小总宽度，n是小数点后的位数
'''

'''
s = 'foobar'
for i, t in enumerate(s):
	print i ,t

s , t = 'foa', 'obr'
print zip(s,t)
'''


'''
string.capitalize()   把字符串的第一个字符大写
string.center(width)  返回一个原字符居中，用空格填充到width的新字符串
string.count(str, beg=0,
end = len(string))    返回str在string里面出现的次数,在beg或者end指定返回str的次数
string.decode(encoding = 'UTF-8',
errors = 'strict')    以encoding指定的编码格式解码string
string.encode(encoding = 'UTF-8',
errors = 'strict')    以encoding指定的编码格式string
string.endswith(obj,beg =0,
        end = len(string)) 检查字符串是否以obj结束
string.expandtabs(tabsize = 8) 把字符串中的tab符号转为空格
string.find(str,beg =0 
end = len(strning)) 检查str是否包含在string中,返回开始的索引
string.index(str, beg = 0,
end = len(string))  同find
string.isalnum()   判断所有字符是不是都是数字
string.isalpha()   判断是不是均为字母
string.isdecimal()   判断是否只包含十进制数字
string.isdigit()     判断是否只包含数字
string.islower()     判断是否均为小写字母
string.isnumeric()   数字字符
string.isspace()     判断是否只包含空格
string.istitle()     判断是不是标题化的
string.isupper()     判断是不是均为大写
string.join(seq)     合并为一个行的字符串
string.lower()       转化为均为小写
string.lstrip()      截掉string左边的空格
string.partition(str)将string分成一个3元素的元组
string.replace(str1,str2,
num = string.count(str1)) 把str1替换成str2 替换不超过num次
string.rfind(str,beg=0,end=len(string))从右边开始查找
string.rindex(str,beg=0,end = len(string))
string.split(str="",num = string.count(str)) 以str为分隔符切片
string.startswith(obj, beg=0, end=len(string))检查是不是以obj开头
string.swapcase()翻转大小写
'''


'''

ASCII      美国标准信息交换码
BMP        基本多文种平面
BOM        直接顺序标记
CJK/CJKV   中文-日文-韩文的缩写
Code point 代表Unicode字符的值
Octet      八位二进制数的位组
UCS        通用字符集
UCS2       UCS的双字节编码方式
UCS4       UCS的四字节编码方式
UTF        Unicode或者UCS的转换格式
UTF-8      8位UTF转换格式
UTF-16     16位UTF转换格式
'''

'''
An enample of reading and writing Unicode string:Writes
a Unicode string to a file in utf-8 and reads itback in.
'''

'''
CODEC = 'utf-8'
FILE  = 'uncode.txt'


hello_out = u"Hello world\n"
bytes_out = hello_out.encode(CODEC)
f = open(FILE,"w")
f.write(bytes_out)
f.close()

f = open(FILE,"r")
bytes_in = f.read()
f.close()
hello_in = bytes_in.decode(CODEC)
print hello_in
'''

'''
module           explain
string           字符串操作的相关函数
re               正则表达式
struct           字符串和二进制之间的转换
c/String10       字符串缓冲对象
base64           Base16,32,64数据编解码
codecs           解码器注册和基类
crypt            进行单方面加密
difflib          找出序列间的不同
hashlib          多种不同安全哈希算法和信息摘要算法的API
hma              HMAC信息鉴权算法的python实现
md5              RSA的MD5信息摘要鉴权
rotor            提供多平坦的加解密服务
sha              NIAT的安全哈希算法
stringprep       提供用于IP协议的Unicode字符串
textrap          文本打包和填充
unicodedata      Unicode数据库
'''

'''
s = ['They','stamp','them','when',"they're",'small']
for t in reversed(s):
	print t
'''

'''
list.append(obj)       向列表中添加一个对象obj
list.count(obj)        返回一个对象obj在列表中出现的次数
list.extend(seq)       把序列seq的内容添加到列表中
list.index(obj, i=0
j = len(list))         返回list[k] == obj 的k值，并且k的范围在i到j
list.insert(index,obj) 在索引值为index的位置插入对象obj
list.pop(index = -1)   删除并返回指定位置的对象
list.remove(obj)       从列表中删除对象obj
list.reverse()         原地翻转列表
list.sort(func=None,key=None,
reverse=False)         以指定的方式排序列表中的成员
'''


#堆栈的建立
'''
stack = []

def pushit():
	stack.append(raw_input('Enter new string: ').strip())

def popit():
	if len(stack) == 0:
		print 'Cannot pop from an empty stack'
	else:
		print 'Removed[', stack.pop(), ']'

def  viewstack():
	print stack

CMDS = {'u':pushit, 'o':popit,'v':viewstack}

def  showmenu():
	pr ="""
	p(U)sh
	p(O)p
	(V)iew
	(Q)uit

	Enter choice:"""

	while  True:
		while  True:
			try:
				choice = raw_input(pr).strip()[0].lower()
			except(EOFError,KeyboardInterrupt,IndexError):
				choice = 'q'

			print'\nYou picker:[%s]' %choice
			if choice not in 'uovq':
				print 'Invalid option, try again'
			else:
				break
		if choice == 'q':
			break
		CMDS[choice]()

if __name__ == '__main__':
	showmenu()
'''


#队列的建立

'''
queue = []

def enQ():
	queue.append(raw_input("Enter new String:").strip())

def deQ():
	if len(queue) == 0:
		print 'Cannot pop from an empty queue'
	else:
		print 'Removed[', queue.pop(0) ,']'

def viewQ():
	print queue

CMDS = {'e':enQ, 'd': deQ, 'v':viewQ}


def  showmenu():
	pr = """
	(E)nqueue
	(D)equeue
	(V)iew
	(Q)uit 

	Enter choice:"""

	while  True:
		while True:
			try:
				choice = raw_input(pr).strip()[0].lower()
			except(EOFError,KeyboardInterrupt,IndexError):
				choice == 'q'
			if choice not in 'devq':
				print"Invalid option, try again"
			else:
				break
		pass

		if choice == 'q':
			break
		else:
			CMDS[choice]()
	pass

if __name__ == '__main__':
	showmenu()
'''

#元组为不可变对象，但其包含的可变对象可以实现改变
#所有的多对子昂，逗号分隔的，未有明确符号定义的，默认类型均为元组

'''
print type(('abc'))
print type(('abc',))
'''

'''

模块        内容
copy        提供浅拷贝和深拷贝的能力
operator    包含函数调用形式的序列操作符
re          Perl风格的正则表达式
StringIO/
cStringIO   把长字符串作为文件来操作
Textwrap    用做包裹/填充文本的函数，也有一个类
types       包含Python支持的所有类型
collections 高性能容器数据类型

'''


#浅拷贝和深拷贝

#浅拷贝：新创建了一个类型和原对象一样，其内容是原来对象元素的引用
#(1)完全切片操作[:] (2)利用工厂函数 (3)使用copy模块中的copy函数

'''
person = ['name',['saving',100.00]]
hubby = person[:]
wifey = list(person)
print [id(x) for x in person,hubby,wifey]
hubby[0] = 'joe'
wifey[0] = 'jone'
hubby[1][1] = 50.0
print hubby, wifey
'''
#由于列表的第一项是不可变对象，第二个对象是可变对象
#所以对于第一项显示拷贝创建了一个新的对象，对于第二个对象则是引用
'''
print[id(x) for x in hubby]
print[id(x) for x in wifey]
'''
#深拷贝(完全分离两个对象)
'''
person = ['name',['saving',100.00]]
hubby = person
import copy
wifey = copy.deepcopy(person)
print [id(x) for x in person,hubby,wifey]
hubby[0] = 'joe'
wifey[0] = 'jone'
hubby[1][1] = 50.0
print hubby, wifey
'''

'''
第一 非容器类型没有被拷贝一说，浅拷贝使用完全切片操作完成的
第二 如果元组变量只包含原子类型对象，那么他的深拷贝不会进行