#_*_ coding:utf-8 _*_
#迭代序列
'''
#通过序列项迭代
nameList = ['Walter','Nocole','Steven','Henry']
for eachName in nameList:
	print (eachName, "Lim")

#通过序列索引迭代
nameList = ['Cathy','Terry','Joe','Heather','Lucy']
for nameIndex in range(len(nameList)):
	print ("Liu",nameList[nameIndex])	

#使用项和索引迭代
nameList = ['Donn','Shirley','Ben','Janice','David','Yen','Wendy']
for i, eachLee in enumerate(nameList):
	print("%d %s Lee" %(i+1, eachLee))
'''

'''
albums = ('Poe','Gaudi','Freud','Poe2')
years = (1976,1987,1990,2003)
for album in sorted(albums):
	print(album)

for album in reversed(albums):
	print(album)

for i, album in enumerate(albums):
	print (i , album)

for album, yr in zip(albums,years):
	print (yr, album)
'''

#迭代器
'''
1.提供了可扩展的迭代器接口
2.对列表迭代带来了性能上的增强
3.在字典迭代中性能提升
4.创建真正的迭代接口，而不是原来的随机对象访问
5.与所有已经存在的用户定义的类以及扩展的模拟序列和映射的对象向后兼容
6.迭代非序列额集合（例如映射和文件）时，可以创建更简洁可读的代码
'''

#创建迭代对象
'''
iter(func, sentinel)
iter(obj)
'''

'''
f = open('hhg.txt','r');
i = len([word for line in f for  word in line.split()])
print (i)	
import os
print (os.stat('hhg.txt').st_size)
f.seek(0) #回到文件头
sum([len(word) for line in f for word in line.split()])
'''

'''
rows = [1,2,3,17]
def  cols():
	yield 56
	yield 2
	yield 1
	pass

x_product_pair = ((i,j) for i in rows for j in cols())
for pair in x_product_pair:
	print (pair)
'''

'''
f = open('hhg.txt','r')
longest = 0;
allLine = [x.strip() for x in f.readlines()]
f.close()
for line in allLine:
	linelen = len(line)
	if linelen > longest:
		longest = linelen
print (longest)
'''