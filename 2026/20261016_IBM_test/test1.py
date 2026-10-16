#!/bin/python3

import math
import os11
import random
import re
import sys

#
# Complete the 'optimizeInAppUpgrades' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY upgradeCosts
#  2. INTEGER budget
#

def optimizeInAppUpgrades(upgradeCosts, budget):
    MOD = 10**9 + 7
    total_enhancement = 0
    n = len(upgradeCosts)
    
    # Greedily pick higher-index upgrades first since 2^i is greater 
    # than the sum of all lower-index upgrades combined.
    for i in range(n - 1, -1, -1):
        if budget >= upgradeCosts[i]:
            budget -= upgradeCosts[i]
            total_enhancement = (total_enhancement + pow(2, i, MOD)) % MOD
            
    return total_enhancement

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    upgradeCosts_count = int(input().strip())

    upgradeCosts = []

    for _ in range(upgradeCosts_count):
        upgradeCosts_item = int(input().strip())
        upgradeCosts.append(upgradeCosts_item)

    budget = int(input().strip())

    result = optimizeInAppUpgrades(upgradeCosts, budget)

    fptr.write(str(result) + '\n')

    fptr.close()