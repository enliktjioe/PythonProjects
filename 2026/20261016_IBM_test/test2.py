#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'toolchanger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY tools
#  2. INTEGER startIndex
#  3. STRING target
#

def toolchanger(tools, startIndex, target):
    n = len(tools)
    min_moves = float('inf')
    
    for i, tool in enumerate(tools):
        if tool == target:
            # Calculate distance moving right and left
            dist_right = (i - startIndex) % n
            dist_left = (startIndex - i) % n
            
            # Find the minimum moves for this specific occurrence
            moves = min(dist_right, dist_left)
            
            # Keep track of the global minimum
            if moves < min_moves:
                min_moves = moves
                
    return min_moves

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tools_count = int(input().strip())

    tools = []

    for _ in range(tools_count):
        tools_item = input()
        tools.append(tools_item)

    startIndex = int(input().strip())

    target = input()

    result = toolchanger(tools, startIndex, target)

    fptr.write(str(result) + '\n')

    fptr.close()