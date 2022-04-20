from decimal import Decimal
import os

with open('D:\\Users\\iopc\\Desktop\\cp_rho_COVALENT.cpc') as f:
    content = f.readlines()

for number, line in enumerate(content):
    if 'l1, l2, l3' in line:
        l1 = line.split()[0]
        l2 = line.split()[1]
        l3 = line.split()[2]
        newline = '                                        ' + \
                str(round((Decimal(l1) / Decimal(24.0988)), 6)) + '  ' + \
                str(round((Decimal(l2) / Decimal(24.0988)), 6)) + '  ' + \
                str(round((Decimal(l3) / Decimal(24.0988)), 6)) + \
                '  l1, l2, l3\n'
        content[number] = newline
        rho = round(Decimal(content[number+1].split()[0]) / Decimal(6.7483), 6)
        newnewline = '                                                                  ' + str(rho) + '    RHO     \n'
        content[number+1] = newnewline


with open('D:\\Users\\iopc\\Desktop\\cp_rho_COVALENT_AU.cpc', 'w') as f:
    f.writelines(content)
    
