#!/usr/bin/python
#encoding=utf-8
#Author:Vi

import os
import os.path
import sys
import hashlib

def FindFile(rootpath, fileseq, delseq):
	dirs = os.listdir(rootpath)
	for dir in dirs:
		path = rootpath + os.sep + dir
		if os.path.isdir(path):
			FindFile(path, fileseq, delseq)
		else:
			MD5Check(path, fileseq, delseq) 

def MD5Check(path, fileseq, delseq):
	f = file(path, 'rb')
	md5 = hashlib.md5()
	md5.update(f.read())#读取path md5值
	if md5.hexdigest() in fileseq:
		delseq.append(path)
	else:
		fileseq.append(md5.hexdigest())
	f.close()
	
def main():
	fileseq = []
	delseq = []
	print u"*****************************文件去重**************************".encode("GBK")
	while True:
		if len(sys.argv) == 1:
			rootpath = raw_input(u"请输入要检查的目录:".encode("GBK"))
		else:
			rootpath = sys.argv[1]
		try:
			FindFile(rootpath, fileseq, delseq)
		except(OSError):
			print u"目录不可达，请检查目录是否存在或输入是否有误！".encode("GBK")
			del sys.argv[1:]
			continue
		break
	
	if len(delseq) == 0 :
		print u"没有查找到重复文件！".encode("GBK")
	else:
		print u"查找到下列重复文件！:".encode("GBK")
		for delfile in delseq:
			print delfile
		while True:
			answer = raw_input (u"是否删除这些重复文件？是（Y/Yes） 否（N/No）".encode("GBK"))
			answer.lower
			if answer in ('y','yes'):
				for delfile in delseq:
					try:
						os.remove(delfile)
					except(OSError):
						print '"%s"' % delfile
						print u"不存在！".encode("GBK")
						continue
				print u"所有重复文件已经删除！".encode("GBK")
				break
			elif answer in ('no','n'):
				print u"没有删除任何文件！".encode("GBK")
				break
			else:
				print u"请选择是否删除这些重复文件？是（Y/Yes）".encode("GBK")

if __name__ == "__main__":
	main()
sys.exit()
