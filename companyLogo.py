#!/bin/python3

import math
import os
import random
import re
import sys
    

if __name__ == '__main__':
    s = input()

charDict = {}

for i in range(len(s)):
    if s[i] in charDict:
        charDict[s[i]] = charDict[s[i]] + 1
    else:
        charDict[s[i]] = 1
 
outList = []        

for i in range(3):
    most = ('z', 0)
    for j in charDict:
        if charDict[j] > most[1]:
            most = (j, charDict[j])
            
        elif charDict[j] == most[1]:
            if j < most[0]:
                most = (j, charDict[j])
                
    outList.append(most)
    charDict.pop(most[0])
    
print(outList[0][0], outList[0][1])
print(outList[1][0], outList[1][1])
print(outList[2][0], outList[2][1])
