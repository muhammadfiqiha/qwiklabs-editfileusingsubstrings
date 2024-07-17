# Script

## findJane.sh
### Description
* This script should catch all jane lines and store them in another text file called oldFiles.txt
### Steps
* Create the oldFiles.txt
* Use grep to look for pattern **jane** in ~/data/list.txt and use it as an input for cut to get the path only and store it in the variable
* Use for loop and iterate for each line in previous variable
* Check the path if exist in the filesystem, if exist then insert it to oldFiles.txt

## changeJane.py
### Description
* This script should takes oldFiles.txt as a command line argument and then renames files with the new username **jdoe**
### Steps
* Import necessary module (sys and subprocess) to use it in the script. The sys (System-specific parameters and functions) module provides access to some variables used or maintained by the interpreter and to functions that interact with the interpreter. The subprocess module allows you to spawn new processes, connect to their input/output/error pipes, and get their return codes.
* Open the file (from argument) using 'with open'
* Use for loops to iterate each line of the file and using .readlines() to read all the file's content
* Fetch the path name and store it to variable and remove unnecessary whitespaces or newlines using .strip()
* Replace the **jane** in path name to **jdoe** using .replace()
* Run the mv command to rename the file using subprocess.run()