#!encoding:utf-8
import pexpect
def run(user,host,password,command):
	"""..."""
	ssh_newkey='Are you sure you  want to continue connecting'
	child=pexpect.spawn('ssh -l %s %s %s' % (user,host,command))
	i=child.expect([pexpect.TIMEOUT,ssh_newkey,'password: '],timeout=5))
	if i==0:
		print 'ERROR!'
		print 'SSH 无法登录，错误为'
		print child.before,child.after
		return None
	if i==1:
		child.sendline('yes')
		child.expect('password:')
		i=child.expect([pexpect.TIMEOUT,'password:'])
		if i==0:
			print 'error!'
			print 'SSH 无法登录，错误为'
			print child.before,child.after
			return None
	child.sendline(password)
	return child
def main():
	host=raw_input('Hostname:')
	user=raw_input('User:')
	password = getpass.getpass()
	command=raw_input('Enter the password:')
	child = run(user,host,password,command)
	child.expect(pexpect.EOF)
	print child.before

if __name__='__main__':
	try:
		main()
	except  Exception,e:
		print str(e)
		traceback.print_exc()
		os.exit(1)
