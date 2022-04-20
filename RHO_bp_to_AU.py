with open('D:\\Users\\iopc\\Desktop\\bp_rho_COVALENT.bpc') as f:
    content = f.readlines()

for number, line in enumerate(content):
    if 'rhoCP' in line:
        rho = str(round(float(line.split()[6]) / 6.7483, 6))
        new_line = line[:30] + rho + line[38:]
        content[number] = new_line


with open('D:\\Users\\iopc\\Desktop\\bp_rho_COVALENT_AU.bpc', 'w') as f:
    f.writelines(content)