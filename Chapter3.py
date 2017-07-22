# -*- coding: utf-8 -*-

#check conditions 
'''
if(wheather_is_hot == 1) and\
(shark_warnings == 0):
'''

#(x,y,z) = (1,2,'a string')

#模块结构和布局
'''
(1)起始行
(2)模块文档  modeule.__doc__
(3)模块导入  
(4)变量定义
(5)类定义  class.__doc__
(6)函数定义  function.__doc__
(7)主程序
'''

#/usr/bin/env python   (startup line)
'''
"this is a test module"  (module documentation)
 
import sys               (module imports)
import os 

debug = True              ((Global)Variable declarations)

class FooClass (object):   (Class declarations )
	'Foo class'
	pass

def test():                 (Function declarations)
	'Test function'
	foo = FooClass()
	if debug:
		print 'ran test()'

if __name__ == '__main__': (main body)
	test()
'''
'''
#!/usr/bin/env python
'makeTextFile.py -- create text file'

import os
ls = os.linesep

#get Filename
fname = raw_input('> ')
while  True:
	if os.path.exists(fname):
		print "Error:'%s' already exists" % fname
	else:
		break
#get file content (text) lines
all = []
print "\nEnter lines('.' by itself to quit).\n"
# loop until user terminates input
while True:
	entry = raw_input('> ')
	if entry == '.':
		break
	else:
		all.append(entry)

fobj = open(fname,'w')
fobj.writelines(['%s%s' %(x,ls)for x in all])
fobj.close()
print"DONE"
'''

#get Filename

fname = raw_input('Enter Filename: ')

try:
	fobj = open(fname,'r')
except IOError, e:
	print"*** file open error:",e
else:
	#display contents to the screen
	for eachLine in fobj:
		print eachLine
	fobj.close()


'''
Debugger: pdb
Logger: logging
profilers:profile, hotshot, cProfile
'''
