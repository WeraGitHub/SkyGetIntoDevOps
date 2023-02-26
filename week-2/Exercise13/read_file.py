# slurping
lines = open('pelican.txt').read()
print(lines)
print(type(lines))


list_lines = lines.splitlines()
print(type(list_lines))
print(len(list_lines))


for line in open('pelican.txt'):
    print(line, end="")
