#!/usr/bin/env python
import sys,os,time,subprocess,random

file_name = 'log.log'
file_path = '/root/www/github-record-script/'
file_log_path = file_path + 'log/'

def check_file():
	if not os.path.exists(file_log_path + file_name):
		f = open(file_path + file_name,'w')
		f.write(str(time.time()) + '\n')
		f.close()

def add_file_line():
	f = open(file_log_path + file_name,'a+')
	f.write(str(time.time()) + '\n')
	f.close()

def git_add():
	cmd = ['git', 'add', '.']
	p = subprocess.Popen(cmd,cwd=file_path)
	print p.wait()

def git_commit():
	centext = "'upload bug info - " + str(time.time()) + "'"
	cmd = ['git', 'commit', '-m',centext]
	p = subprocess.Popen(cmd,cwd=file_path)
	print p.wait()

def git_push():
	cmd = ['git', 'push', '-u','origin','master']
	p = subprocess.Popen(cmd,cwd=file_path)
	print p.wait()
		
def file_handle():
	check_file()
	add_file_line()
	git_add()
	git_commit()
	git_push()

if __name__ == "__main__":
	file_handle()	
	print 'done.'