


def PackAbs(call,pos):
	partitions=call.split('.')
	package=''
	for i in range (0,len(partitions)):
		if partitions[i] in pos[i]: #
			package=package+partitions[i]+'.'
		else:
			if package=="" or package=='com.':
				package=None
			else:
			        if package.endswith('.'):
			    		package=package[0:-1]
    			break
			#if package=='com.':
			#	package=None
			#break
	return package
