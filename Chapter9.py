#_*_ coding:utf-8_*_
#file_object = open(file_name, access_mode = 'r', buffering = -1)
#UNS 通用换行符支持
#删除行结束符
'''
f = opne('MyFile','r')
data = [line.strip() for line in f.readlines()]
f.close()
'''

#文件中移动
#seek()

'''
os模块属性   描述
linesep      用于在文件中分隔行的字符串
sep          用于分隔文件路径名的字符串
pathsep      用于分隔文件路径的字符串
curdir       当前工作目录的字符串名称
pardir       （当前工作目录的）父目录字符串名称
'''

'''
filename  = raw_input('Enter file name: ')
fobj = open(filename,'w')
while True:
	aLine = raw_input("Enter a line('.' to quit): ")
	if aLine != ".":
		fobj.write("%s%s",(aLine,os.linesep))
	else:
		break
fobj.close()
'''

'''
文件对象的方法         操作
file.close()           关闭文件
file.fileno()          返回文件的描述符
file.flush()           刷新文件的内部缓冲区
file.isatty()          判断file是否是一个类tty设备
file.next()            返回文件的下一行
file.read(size=-1)     从文件读取size个字节
file.readline(size=-1) 从文件中读取并返回一行
file.readlines(sizhint=0) 读取文件所有行并作为一个列表返回
file.xreadlines()       用于迭代
file.seek()            移动文件指针
file.tell()             返回当前在文件中的位置
file.truncate()        截取文件到追到size字节
file.write(str)        向文件中写入字符串
file.writelines(seq)    向文件中写入字符串seq
'''

'''
import sys
print ('you entered', len(sys.argv), 'arguments...')
print ('they were:', str(sys.argv))
'''

'''
表 9.5 os 模块的文件/目录访问函数
函数 描述
文件处理
mkfifo()/mknod() a 创建命名管道/创建文件系统节点
remove()/unlink() Delete file 删除文件
rename()/renames() b  重命名文件
*stat c() 返回文件信息
symlink() 创建符号链接
utime() 更新时间戳
tmpfile() 创建并打开('w+b')一个新的临时文件
walk() a 生成一个目录树下的所有文件名
目录/文件夹
chdir()/fchdir() a 改变当前工作目录/通过一个文件描述符改变当前工作目录
chroot() d 改变当前进程的根目录
listdir() 列出指定目录的文件
getcwd()/getcwdu() a 返回当前工作目录/功能相同, 但返回一个 Unicode 对象
mkdir()/makedirs() 创建目录/创建多层目录
rmdir()/removedirs() 删除目录/删除多层目录
访问/权限
access() 检验权限模式
chmod() 改变权限模式
chown()/lchown() a 改变 owner 和 group ID/功能相同, 但不会跟踪链接
umask() 设置默认权限模式
文件描述符操作
open() 底层的操作系统 open (对于文件, 使用标准的内建 open() 函数)
read()/write() 根据文件描述符读取/写入数据
dup()/dup2() 复制文件描述符号/功能相同, 但是是复制到另一个文件描述符
设备号
makedev() a 从 major 和 minor 设备号创建一个原始设备号
major() a /minor() a 从原始设备号获得 major/minor 设备号
a. New in Python 2.3.
b. New in Python 1.5.2.
c. Includes stat(), lstat(), xstat().
d. New in Python 2.2.
表 9.6 os.path 模块中的路径名访问函数
函数 描述
分隔
basename() 去掉目录路径, 返回文件名
dirname() 去掉文件名, 返回目录路径
join() 将分离的各部分组合成一个路径名
split() 返回 (dirname(), basename()) 元组
splitdrive() 返回 (drivename, pathname) 元组
splitext() 返回 (filename, extension) 元组
信息
getatime()  返回最近访问时间
getctime()  返回文件创建时间
getmtime()  返回最近文件修改时间
getsize() 返回文件大小(以字节为单位)
查询
exists() 指定路径(文件或目录)是否存在
isabs() 指定路径是否为绝对路径
isdir() 指定路径是否存在且为一个目录
isfile() 指定路径是否存在且为一个文件
islink() 指定路径是否存在且为一个符号链接
ismount() 指定路径是否存在且为一个挂载点
samefile() 两个路径名是否指向同个文件
'''

'''
import os
for tmpdir in ('/tmp',r'c:\temp'):
	if os.path.isdir(tmpdir):
		break
	else:
		print 'no temp directory available'

tmpdir = ''
if tmdir:
	os.chdir(tmpdir)
	cwd = os.getcwd()
	print '*** current temporary directory'
	print cwd

print'*** creating example directory...'
os.mkdir('example')
os.chdir('example')
cwd = os.getcwd()
print '*** new working directory:'
print cwd
print '*** creating test file...'
fobj = open('test','w')
fobj.write('foo\n')
fobj.write('bar\n')
fobj.close()

print'*** updated directory listing'
print os.listdir(cwd)

print "*** renaming 'test ' to firsttest.txt'"
os.rename('rest','filetest.txt')
print'*** updated directory listing:'
print os.listdir(cwd)

path = os.path.join(cwd, os.listdir(cwd)[0])
print'*** full file pathname'
print path
print'***(pathname,basename)=='
print os.path.split(path)
print '***(filename,extension)=='
print os.path.splitext(os.path.basename(path))

print '***displying file contents:'
fobj = opne(path)
for eachLine in fobj:
	print eachLine,
	fobj.close()

print '*** deleting test file'
os.remove(path)
print '***updated directory listing:'
print os.listdir(cwd)
os.chdir(os.pardir)
print'*** deleting test directory'
os.rmdir('example')
print'***DONE'
'''

#利用pickle 以及 marshal模块实现永久存储
