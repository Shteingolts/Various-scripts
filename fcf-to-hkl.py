with open('D:\\Users\\iopc\\Desktop\\111.txt') as f:
    content = f.readlines()

new_content = ''
for line in content:
    try:
        new_line = line.split()[0] + '  ' + line.split()[1] + '  ' + line.split()[2] + '  ' + line.split()[4] + '  ' + line.split()[5] + '  ' + '\n'
        new_content = new_content + new_line
    except: IndexError

with open('D:\\Users\\iopc\\Desktop\\123.txt', 'w') as f:
    f.write(new_content)