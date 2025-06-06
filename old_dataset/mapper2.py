#!/usr/bin/env python3
# -*-coding:utf-8 -*
import sys

for line in sys.stdin:
    line = line.strip();
    columns = line.split(',') # split line into list 
    if columns[9] == "True":
        try:
            print(f"{columns[7]}\t1")
        except ValueError:
            pass