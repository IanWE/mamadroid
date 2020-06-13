from time import time
import csv
import os
import subprocess
import numpy as np

# Changes calls format. Previous format for each line is 'APICallX'===>['NextCall1','NextCall2'...] according to all the times APICallX is called. The resulting file will have each line as 'APICallX'\t'NextCall1'\t'NextCall2'\t... 
def main (WHICHSAMPLES,wf):#dbs,N
	alldb=[]
	allapps=[]
	for v in range (0,len(WHICHSAMPLES)):
		onedb=[]
		numApps=os.listdir('graphs/'+WHICHSAMPLES[v]+'/')#list samples
		#numApps=os.listdir('graphs/')

		allapps.append(numApps)##samples
		leng=len(numApps)
		Fintime=[]
		checks=[0,999,1999,2999,3999,4999,5999,6999,7999,8999,9999,10999,11999,12999]
		for i in range (0,len(numApps)):
			if i in checks:
				print 'starting ',i+1,' of ',leng
                                print "graphs/"+numApps[i]
			with open('graphs/'+WHICHSAMPLES[v]+'/'+str(numApps[i])) as callseq:
			#with open('graphs/'+str(numApps[i])) as callseq:
				specificapp=[]
				for line in callseq:
						specificapp.append(line)
				callseq.close()

			call=[]
			nextblock=[]
			nextcall=[]
			Startime= time()
			for line in specificapp:
				if (line[0]=='<' and (line[1]=="'" or line[1].isalpha())):
					call.append(str(line.split('(')[0]))
					nextblock.append(str(line.split('==>')[1]))#split into 2 part at ==>

			for j in range (0,len(nextblock)):#store the second part in next call

				supporto=nextblock[j].translate(None, '[]\'\\')
				supporto=supporto.replace('\n','')

				nextcall.append([])
				nextcall[j]=(supporto.split(','))
			Fintime.append(time()-Startime)
			wholefile=[] 
			for j in range (0, len(call)):
				eachline=call[j]+'\t'
				for k in range (0,len(nextcall[j])):
					tagliaparam=nextcall[j][k].split('(')[0]#get function name of nextcall[j][k]
					eachline=eachline+tagliaparam+'\t'
				wholefile.append(eachline)#string list
                                # call1  call2  call3
                                # call2  call3
			if wf=='Y':
				f = open('Calls/'+WHICHSAMPLES[v]+'/'+str(numApps[i]), 'w') 
				for line in wholefile:
					f.write(str(line)+'\n')
				f.close
			onedb.append(wholefile)
		alldb.append(onedb)#alldb has all samples.
        #print alldb,allapps
	return alldb,allapps
			
