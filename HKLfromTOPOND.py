import os

current_path = os.path.dirname(os.path.realpath(__file__))
inputFileName = input('Enter file name without extension: ')

with open(current_path + '\\' + inputFileName + '.outp') as f:
    fileContent = f.readlines()

for index, line in enumerate(fileContent):
    if '  H  K  L   PX     PY     PZ    REAL PART   IMAG. PART    Fhkl' in line:
        fileContent = fileContent[index + 2: -12]

HKL_LINE_WIDTH = 4
F_LINE_WIDTH = 8
newContent = ''
for index, line in enumerate(fileContent):
    F = str(format(float(line.split()[-1]), '.3f'))
    h = line[0:3]
    k = line[3:6]
    l = line[6:9]
    
    new_line = (' '*(HKL_LINE_WIDTH - len(h)) + h +
                ' '*(HKL_LINE_WIDTH - len(k)) + k +
                ' '*(HKL_LINE_WIDTH - len(l)) + l +
                ' '*(F_LINE_WIDTH - len(F)) + F + 
                '  ' + str(0.055) + '\n')
    newContent = newContent + new_line
with open(current_path + '\\' + inputFileName + '.hkl', 'w') as f:
    f.write(newContent)