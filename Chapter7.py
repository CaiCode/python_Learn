#_*_ coding:utf-8_*_
#创建字典
'''
dict1 = {}
dict2 = {'name':'earth', 'port':80}

fdict = dict((['x',1],['y',2]))

ddict = {}.fromkeys(('x','y'),-1)

edict = {}.fromkeys(('foo','bar'))
'''

'''
dict2 = {'name':'earth', 'port':80}
for key in dict2.keys():
	print 'key = %s, value=%s' %(key, dict2[key])
print dict2['name']
'''

'''
方法名字        操作
dict.clear()    删除字典中的所有元素
dict.copy()     返回字典（浅复制）的一个副本
dict.fromkeys(seq,
val=None)       创建被返回一个新字典，以seq中的元素做该字典的键
dict.get(key,
default =None)   返回key对应的value的值，不存在则返回default的值
dict.has_key(key) 如果键在字典中存在返回True
dict.items()      返回一个包含字典中对元组的列表
dict.keys()       返回一个包含字典中键的列表
dict.iter()       
dict.pop(key[, default]) 同方法get相同如果Key存在删除并返回dict[key]
dict.setdefault(key,
default =None)    与方法set()相似，如果字典不存在Key键
dict.update(dict2) 将dict2的键-值对添加到字典dict
dict.values()      返回一个包含字典中所有值的列表
'''

'''

db = {}

def  newuser():
	prompt = 'login desired'
	while True:
		name = raw_input(prompt)
		if db.has_key(name):
			prompt = 'name taken, try another: '
			continue
		else:
			break
		pwd = raw_input('passwd: ')
		db[name] = pwd
		pass
	pass

def  olduser():
	name = raw_input('login: ')
	pwd = raw_input('passwd: ')
	passwd = db.get(name)
	if passwd == pwd:
		print 'welcome back', name
	else:
		print 'login incorrect'
	pass


def  showmenu():
	prompt = """
	(N)ew User Login
	(E)xisting User Login
	(Q)uit
	Enter choice:"""

	done = False
	while not done:

		chosen = False
		while  not chosen:
			try:
				choice = raw_input(prompt).strip()[0].lower()
			except(EOFError,KeyboardInterrupt):
				choice = 'q'
			print '\nYou picked: [%s]' %choice
			if choice not in 'neq':
				print 'invalid option, try again'
			else:
				chosen = True
				done = True
newuser()
olduser()

if __name__ == '__main__':
	showmenu()
'''

'''
s = set('cheeseshop') 可变集合
print (s)
'''

#t = frozenset(['bookshop'])  不可变集合

'''
s = set('cheeseshop')
s.add('z')
s.update('pypi')
s.remove('z')
s -= set('pypi')
'''

'''
方法名称         操作
s.issubset(t)    判断s是否是t的子集
s.issuperse(t)   判断t是否是s的超集
s.union(t)       返回s和t的并集
s.intersection(t)返回s和t的交集
s.difference(t)  返回一个集合是s的成员，但不是t的成员
s.symmertric_difference(t) 返回一个集合非s和t共有的成员
s.copy()          返回集合s的浅复制
