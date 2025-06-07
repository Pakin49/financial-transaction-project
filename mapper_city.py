#!/usr/bin/env python3
import sys

def clean_amount(snum):
    negative = False
    res = ""
    for char in snum:
        if char == "$":
            continue
        if char == "-":
            negative = True
            continue
        res += char
    clean_num = float(res)
    if negative:
        clean_num *= -1 
    return clean_num

for line in sys.stdin:
    line = line.strip()
    columns = line.split(",")
    if columns[0] == "id":
        continue
    if len(columns) == 12:
        merchant_state = columns[8]
        amount = clean_amount(columns[4])
        if merchant_state and merchant_state != "":
            try:
                print(f"{merchant_state}\t1\t{amount}")
            except ValueError:
                pass
