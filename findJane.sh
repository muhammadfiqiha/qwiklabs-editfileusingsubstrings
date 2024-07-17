#!/bin/bash

# create file oldFiles.txt
> oldFiles.txt

# grab file names associated with username jane
files=$(grep " jane " ~/data/list.txt | cut -d " " -f 3)

# for loop to test each file name in files variable exists
for file in $files;
do
  # check if file exist
  if test -e /home/student$file; then
    # if exist then insert/append the file name to oldFiles.txt
    echo /home/student$file >> oldFiles.txt
  fi
done