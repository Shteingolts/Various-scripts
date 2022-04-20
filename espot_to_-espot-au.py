path_to_file = "D:\\Users\\iopc\\Desktop\\3D_map_ESPOT.dat"
path_to_new_file = "D:\\Users\\iopc\\Desktop\\3D_map_-ESPOTau.dat"

with open(path_to_file) as f:
    content = f.readlines()

transformed_content = []
constant = 0.529177
for line in content:
    if line.isspace():
        continue
    transformed_value = -(float(line.split()[3]) * constant)
    new_line_tuple = (line[:42], "    ", str(transformed_value), "\n")
    new_line = "".join(new_line_tuple)
    transformed_content.append(new_line)


with open(path_to_new_file, "w") as f:
    f.writelines(transformed_content)
