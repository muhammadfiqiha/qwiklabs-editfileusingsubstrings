#!/usr/bin/env python3

import sys
import subprocess

# read the file from argument 1
with open(sys.argv[1]) as f:
    # for loop to iterate each line of f
    for line in f.readlines():
        # remove any whitespaces or newlines and fetch the old name
        old_filename = line.strip()
        # use .replace() to replace 'jane' with 'jdoe'
        new_filename = old_filename.replace("jane", "jdoe")
        # run the mv command using subprocess to rename the file
        subprocess.run(['mv', old_filename, new_filename])

# close the file
f.close()