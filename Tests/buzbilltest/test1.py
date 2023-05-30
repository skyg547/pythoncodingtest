#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the braces function below.
def braces(values):
    answer = []

    for i in values:
        tempstack = []
        breaknum = 0

        for j in i:

            if tempstack:
                print(tempstack, '1', j)

                if j == ')':
                    temp = tempstack[-1]
                    if '(' != temp:
                        answer.append('NO')
                        breaknum = 1
                        break
                    elif temp == '(':
                        tempstack.pop()



                elif j == '}':
                    temp = tempstack[-1]
                    if '{' != temp:
                        answer.append('NO')
                        breaknum = 1

                        break
                    elif temp == '{':
                        tempstack.pop()



                elif j == ']':
                    temp = tempstack[-1]
                    if '[' != temp:
                        answer.append('NO')
                        breaknum = 1

                        break
                    elif temp == '[':
                        tempstack.pop()

                else:
                    tempstack.append(j)
            else:
                tempstack.append(j)

        if breaknum == 1:
            continue

        if not tempstack:
            answer.append('YES')
        else:
            answer.append('NO')

    return answer


s = ['[()]',
     '[{}]']

for i in braces(s):
    print(i)
# print(braces(s))
