#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip();
    columns = line.split(',') # split line into list 
    if columns[9] == "True":
        try:
            print(f"{columns[6]}\t1") #merchat_type
            #print(f"{columns[7]}\t1") #country
        except ValueError:
            pass
