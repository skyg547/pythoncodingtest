from itertools import permutations


def largestMagical(binString):
    binarray = []

#좋은 문자열을 찾기 how 0
    templist = ''
    cnt = 0
    for i in binString:

        if i == '1':
            cnt += 1
            templist += '1'
        elif i == '0':
            cnt -= 1
            templist += '0'
        if cnt == 0 and templist != []:
            binarray.append(templist)
            cnt = 0
            templist = ''

    return max(list(map(''.join, permutations(binarray))))



# Write your code here
1111000110010110100110101001011000
101011101001001100101011100011010101011101000100
11010111001010010101100101100110010101001110011000
11011000111100011110000011100111000011011111000000
11011110111100011110000011100111000011000111000000
10101010101010101010101010101010101010101010101010

binString = '11011000'

print(largestMagical(binString))
