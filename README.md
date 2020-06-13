MaMaDroid Source Code
=============================
**Authors:** Enrico Mariconti, Lucky Onwuzurike, Panagiotis Andriotis, Emiliano De Cristofaro, Gordon Ross, Gianluca Stringhini (2017).

This is the infrastructure we developed for MaMaDroid, as presented in the paper below. If you use the infrastructure in your work, please cite or acknowledge us (_bib_ entry follows).

```text
@inproceedings{MaMaDroid,
  title={{MAMADROID: Detecting Android Malware by Building Markov Chains of Behavioral Models}},
  author={Mariconti, Enrico and Onwuzurike, Lucky and Andriotis, Panagiotis and De Cristofaro, Emiliano and Ross, Gordon and Stringhini, Gianluca},
 booktitle={{Proceedings of the Annual Symposium on Network and Distributed System Security (NDSS)}},
  year={2017}
}
```

Below is a description of the files and subdirectories in the **general** directory. 
As described in the paper, when a dataset is enlarged using new samples, there is no need of re running the old ones. run the new ones in a different folder and then merge the two csv files generated at the end of the procedure.
In the graphs folder there are a few little files results of the static analysis. You can use them to understand the code and do exercise.

Files
=====

* **Appgraph.java** - Java file used for extracting the call graphs in an APK. You need to download the soot jars (see the soot class path) in the code, the sources and sink text file, all of which is available online on the flowdroid site. Add the path of the soot jars to your javac classpath and then compile (or compile with the -cp option).

* **mamadroid.py** - This is the first script to run after succesfully compiling the Appgraph.java file. It runs the Appgraph class which uses soot to generate the call graph. It then parses the call graph using parseGraph.py and finally, abstract the API calls using abstractGrap.py. It accepts two arguments using the -f (or --file ) and -d (or --dir) options which specifies respectively, the APK file (or directory with APK files) to analyze and the path to your Android platform directory. Use the -h option to view the help message. You can also edit the amount of memory allocated to the JVM heap space to fit your machine capabilities.

* **parseGraph.py** This script parses the call egdes i.e., from the call graphs, extracted from an app into the caller and callee(s) API calls.

* **abstractGraph.py** This script first preprocesses the sequences of API calls and then abstracts them to the two different modes of operation i.e., package and family modes. It first abstract a call to its class using the classes.txt as a whitelist of classes before abstracting to the other two modes using the packages.txt and Families.txt files. 

* **MaMaStat.py** - This file is the main script of the system. It has an help on which functionalities it has. Current version is handling options about writing or not the intermediate files in the folders and managing the cores for the point where the mutiprocessing is in use.

* **MarkovCall.py** - uses Markov.py to create the features file for each database. the database will be the folder of the inputs (that are the outputs of the previous script) and it returns a csv file where each line is a sample a part from the first one that is an header line. For stupid reasons and details, it uses as input the Occ.txt files instead of the previous ones.

* **Markov.py** - Used from MarkovCall.py to extract the features related to the Markov model.

* **classes.txt** - List of packages currently updated to Android API level 28 (excluding classes from the new androidx.\* packages). Used in the abstraction and Markov modeling script.

* **packages.txt** - List of classes currently updated to Android API level 28 (excluding the new androidx.\* packages). Used in the abstraction and Markov modeling script.

* **Families.txt** - List of families currently updated to Android API level 28 (excluding the androidx). Used in the abstraction and Markov modeling script.


Subdirectories
==============

They are used for the files generated from the scripts in the **general** directory.

* **user supplied apk directory** - When MaMaDroid analyzes a directory of apk files, it creates a folder with the user-supplied name in the current directory that contains the other directories and their respective content listed below. 

* **graphs** - This folder contains the output of the parsed sequence of API calls of analyzed apps.

* **Calls** - Folder containing reformatted files generated by TxtToCallsCSV.py when the -wf flag is set to Y. They will be in folders with the same name as the ones in graphs.

* **family** - This folder contains files with the sequence API calls of analyzed apps when they are abstracted to families.

* **package** - This folder contains files with the sequence API calls of analyzed apps when they are abstracted to packages.

* **class** - This folder contains files with the sequence API calls of analyzed apps when they are abstracted to classes.

* **Features** - Having subfolders Families and Packages containing the csv files for the list of samples features generated for each dataset through the Markov model.

===================================================================

I met some problem when running its original codes, so I changed some codes.

