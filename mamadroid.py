'''
info: This is the first script to run after succesfully compiling the Appgraph.java file. 
It uses soot to generate the callgraph and parses the graph and abstract the API calls for use by the MaMaStat.py script. 
It accepts two arguments using the -f (or --file ) and -d (or --dir) options which specifies respectively, the APK file 
(or directory with APK files) to analyze and the to your Android platform directory. Use the -h option to view the help message. 
You can also edit the amount of memory allocated to the JVM heap space to fit your machine capabilities.
'''
import glob
import os 
from subprocess import Popen, PIPE
import parseGraph
import shlex
import argparse
import abstractGraph


def parseargs():
	parser = argparse.ArgumentParser(description = "MaMaDroid - Analyze Android Apps for Maliciousness. For optimum performance, run on a machine with more than 16G RAM. Minimum RAM requirement is 4G.")
	parser.add_argument("-f", "--file", help="APK file to analyze or a directory with more than one APK to analyze.", type=str, required=True) 
	parser.add_argument("-d", "--dir", help="The path to your Android platform directory", type=str, required=True)
	args = parser.parse_args()
	return args


def _make_dirs(_base_dir):
	try:
		os.mkdir(_base_dir + "/graphs")
		os.mkdir(_base_dir + "/package")
		os.mkdir(_base_dir + "/family")
		os.mkdir(_base_dir + "/class")
	except OSError:
		print "MaMaDroid Info: One or more of the default directory already exists. Skipping directory creation..."


def _repeated_function(app, _app_dir):
	try:
		if os.path.isfile(app + ".txt"):
			print "MaMaDroid Info: Finished call graph extraction, now parsing..."
			_graphFile = parseGraph.parse_graph(app + ".txt", _app_dir)
			print "MaMaDroid Info: Finished parsing the graph, now abstracting..."
			abstractGraph._preprocess_graph(_graphFile, _app_dir)
			os.remove(app + ".txt")
		else:
			print "MaMaDroid Info: There was an error extracting call graphs from", app
	except Exception, err:
		print "MaMaDroid Info:", err


def main():
	_base_dir = os.getcwd()
	
	apps = parseargs()

	if os.path.isdir(apps.file):
		_apk_dir = apps.file.split("/")[-1]
		if len(_apk_dir) == 0:
			_apk_dir = apps.file.split("/")[-2]
		
		_app_dir = _base_dir + "/" + _apk_dir
		_make_dirs(_app_dir)

		for app in glob.glob(apps.file + "/*.apk"):
			cmd = "java -Xms20g -Xmx50g -XX:+UseConcMarkSweepGC Appgraph " + app + " " + apps.dir
			ran = Popen(shlex.split(cmd))
			while 1:
				check = Popen.poll(ran) 
				if check is not None:		#check if process is still running
					break
			if ran.communicate()[1]:
				_repeated_function(app, _app_dir)
			else:
				_repeated_function(app, _app_dir)

	else:
		_make_dirs(_base_dir)
		cmd = "java -Xms20g -Xmx50g -XX:+UseConcMarkSweepGC Appgraph " + apps.file + " " + apps.dir
		ran = Popen(shlex.split(cmd))
		while 1:
			check = Popen.poll(ran)
			if check is not None:		#check if process is still running
				break
		if ran.communicate()[1]:
			_repeated_function(apps.file, _base_dir)
		else:
			_repeated_function(apps.file, _base_dir)

if __name__ == "__main__":
	main()
