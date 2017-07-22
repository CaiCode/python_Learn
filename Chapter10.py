#_*_ coding:utf-8 _*_
#try-except
'''
try:
	try_suite #watch for enceptions here
except Exception[, reason]:
	except_suite # exception-handling code
'''

'''
def safe_float(obj):
	try:
		retval = float(obj)
	except ValueError:
		retval = 'could not convent non_number to float'
	except TypeError:
		retval = 'object type cannot to converted to float'
	return retval

def safe_float(obj):
	try:
		retrval = float(obj)
	except(ValueError, TypeError):
		retrval = 'error'
	return retrval

try:
	float(['float() does nt ','like lists',2])
except TypeError, diag:
	pass

try:
	try_suite
finally:
	finally_suite #无论如何都执行
'''

#触发异常
#raise
'''
raise exclass    触发一个异常，从exclass生成一个实例
raise exclass()  同上，通过函数调用操作符，生成一个exclass实例
raise exclass, args 同时提供异常参数
raise exclass,args, tb 提供一个追踪对象
raise exclass,instance
raise instance

'''
#断言
#assert expression[,arguments]

'''
import os, socket, errno, types, temfile

class NetworkError(IOError):
	pass

class FileError(object):
	"""docstring for FileError"""
	pass


def updArgs(args, newarg = None):
	if isinstance(args, IOError):
		myargs = []
		myargs.extend([arg for arg in args])
	else:
		myargs = list(args)
	if newarg:
		myargs.append(newarg)
	return tuple(myargs)


def  fileArgs(file, mode, args):
	if args[0] = errno.EACCES and 'access' in dir(os):
		perms = ''
		permd = {'r':os.R_OK, 'w': os.W_OK, 'x': os.X_OK}
		pkeys = permd.keys()
		pkeys.sort()
		pkeys.reverse()
		for eachPerm in 'rwx':
			if os.access(file,permd[eachPerm]):
				perms += eachPerm
			else:
				perms += '-'
		if isinstance(args, IOError):
			myargs = []
			myargs.extend([arg in args])
		else:
			myargs = list(args)
		myargs[1] = "'%s' %s(perms: '%s')"%(mode, myargs[1],perms)
		myargs.append(args.filename)
	else:
		myargs = args

	return tuple(myargs)

def myconnect(sock, host, port):
	try:
		sock.connect((host, port))
	except socket.error, args:
		myargs = updArgs(args)
	if len(myargs) == 1:
		myargs = (errno.ENXIO, myargs[0])

	raise NetworkError, updArgs(myargs, host+ ':' + str(port))

def  myopen(file, mode='r'):
	try:
		fo = open(file,mode):
	except IOError, args:
		raise FileError, fileArgs(file,mode,args)
	return fo
	pass

def testfile():
	file = mktemp()
	f = opne(file, 'w')
	f.close()

	for eachTest in ((0,'r'), (0100,'r'),(0400,'w'),(0500,'w')):
		try:
			os.chmod(file, eachTest[0])
			f = myopen(file, eachTest[1])
		except FileError, args:
			print "%s:%s"(args.__class__ame,args)
		else:
			print file, "opened ok ... perm ignored"
	f.close()
	os.chmod(file, 0777)
	os.unlink(file)


def testnet():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	for eachHost in ('deli','www'):
		try:
			myconnect(s, 'deli',8080)
		except NetworkError, args:
			print "%s:%s"(args.__class__name, args)

if name == '__main__':
	testfile()
	testnet()
'''
