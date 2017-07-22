#2-4

'''
String = raw_input()
#print String
print 15+int(String)
'''

#2-5

'''
num = 0
while num<=10:
	print num
	num += 1
'''

'''
for i in range(10):
	print i
'''

#2-6

'''
Judge_Num = int(raw_input());
if(Judge_Num>0):
	print 'The Number > 0'
elif(Judge_Num<0):
	print 'The Number < 0'
else:
	print 'The Number = 0'
'''

#2-7

'''
String = raw_input()
i = 0
while i< len(String):
	print String[i]
	i += 1
'''

'''
String = raw_input();
for i in String:
	print i
'''

#2-8

'''
import math
AList = [1,23,4,546,8]
print sum(AList)
ATuple = (1,12,34,42,67)
print sum(ATuple)
'''

'''
num_input = raw_input('Please put the number in ')
num_groud = num_input.split(' ')
num_groud_num = [int(i) for i in num_groud]
m_sum = sum(num_groud_num)
print 'The sum is %d'%m_sum
'''

#2-9
'''
AList = [1,2,4,5,6]
print float(sum(AList))/len(AList)
'''

#2-10
#!/usr/bin/python  

'''
while True:
	num = int(raw_input('Please Give a Number: '))
	if num >= 1 and num <= 100:
		print 'Success'
		break
	else:
		print 'The number is wrong'
'''

#2-11
'''
print'\
      (1) Get sum\n\
      (2) Get Average\n\
      (3) Exit\n'


while True:
	choose = int(raw_input("please give your choose "))
	if choose == 3:
		break
	#Get The number
	num_input = raw_input('Please put the number in ')
	num_groud = num_input.split(' ')
	num_groud_num = [int(i) for i in num_groud]
	sum_Num = sum(num_groud_num)
	if choose == 1:
		print 'the sum is ', sum_Num
	if choose == 2: 
		print 'the average is ',  float(sum_Num)/5.0
'''

#2-12

'''
import sys
#print dir(sys)
'''

#2-15
