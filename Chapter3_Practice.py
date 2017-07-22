def WriteInFile():
    import os
    ls = os.linesep
    # get Filename
    fname = raw_input('Please Give Your Filename ')
    while True:
    	if os.path.exists(fname):
    		print "Error:'%s' already exists" % fname
    	else:
    		break
    		# get file content (text) lines
    all = []
    print "\nEnter lines('.' by itself to quit).\n"
    # loop until user terminates input
    while True:
    	entry = raw_input('> ')
    	if entry == '.':
    		break
    	else:
    		all.append(entry)
    fobj = open(fname, 'w')
    fobj.writelines(['%s%s' % (x, ls)for x in all])
    fobj.close()
    print"DONE"

def ReadFile():
	import os
	ls = os.linesep

	fname = raw_input('Enter Filename: ')
	'''
	while True:
		if os.path.exists(fname):
			print "Error:'%s' already exists" % fname
		else:
			break
		pass
	'''
	try:
		fobj = open(fname, 'r')
	except IOError, e:
		print"*** file open error:", e
	else:
		for eachLine in fobj:
			print eachLine.strip()
		fobj.close()

CMDS = {'w':WriteInFile,'r':ReadFile,'q':quit}

def  showmenu():
	pr ="""
	(W)riteInFile
	(R)eadFile
	(Q)uit

	Enter choice:"""

	while  True:
		while  True:
			try:
				choice = raw_input(pr).strip()[0].lower()
			except(EOFError,KeyboardInterrupt,IndexError):
				choice = 'q'

			print'\nYou picker:[%s]' %choice
			if choice not in 'wrq':
				print 'Invalid option, try again'
			else:
				break
		if choice == 'q':
			break
		CMDS[choice]()


if __name__ == '__main__':
	showmenu()