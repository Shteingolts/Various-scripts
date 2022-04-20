#a program that writes Crystal17 inout file for calculating the theoretical structure factors by their hkl indices up to a given index.

import os
current_path = os.path.dirname(os.path.realpath(__file__))
h = int(input("h: "))
k = int(input("k: "))
l = int(input("l: "))
filename = input("filename without extension: ")

with open(str(current_path + '\\' + filename + '.d3'), 'w') as f:
    f.write('XFAC\n')
    totalF = (h*2 +1) * (k*2 +1) * (l*2 +1)
    f.write(str(totalF) + '\n')
    f.write(str(0) + '\n')
    
    for indexL in range(-l, l + 1):
        for indexK in range(-k, k + 1):
            for indexH in range(-h, h + 1):
                f.write(str(indexH) + ', ' + str(indexK) + ', ' + str(indexL) +'\n')
    f.write('END')