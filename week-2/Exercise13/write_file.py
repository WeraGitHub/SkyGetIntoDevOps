append = open('pelican.txt', 'w')
# a for append and w overwrite

num = append.write("A wonderful bird is the pelican,")
print(num)
num = append.write("\nHis bill holds more than his belican")

lines = ["He can take in his beak,\n", "Enough food for a week,\n", "But I'm damned if I see how the helican.\n"]

num = append.writelines(lines)
