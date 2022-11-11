"""
TRUNCATE LARGEST LOG FILE IN A DIRECTORY

Requirement: Bash

Written on: 25 April 2022

Tested on: Linux(debian)

Author: A.S. Faraz Ahmed

Description:

    Sample input: none
    run: python3 linux.py or sh log_file.sh
    
"""
import os

di = [f for f in os.listdir('./') if '.log' in f]
fi_si = [os.stat(i).st_size for i in di]
largest_file = di[fi_si.index(max(fi_si))]

with open(largest_file, mode = 'rb+') as f:
    lines = f.readlines()
if len(lines) > 100:
    with open(largest_file, mode = 'wb+') as f:
        for i in range(len(lines)-100, len(lines)):
            f.write(lines[i])
    print('Largest file is: {} and it is truncated.' .format(largest_file))
