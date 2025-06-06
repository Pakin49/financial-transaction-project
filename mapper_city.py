#!/usr/bin/env python3
import sys
import csv

reader = csv.reader(sys.stdin)
count = 0
for columns in reader :
    if(count==0):
        count+=1
        continue
    if len(columns) > 8 and columns[8].strip()!="":
        try:
            print(f"{columns[8]}\t1") 
        except ValueError:
            print("bruh")
            pass
