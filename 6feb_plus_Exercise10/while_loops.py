# line = None
#
# while line != 'done':
#     line = input('Type "done to complete: ')
#     line = line.lower()
#     print('<<<<<', line, '>>>>>')
#
# print('The end')
import sys

# myl = [0, 67, 32, 9, 77]
#
# while myl:
#     print(myl.pop() * 2)


# names = ['Rod', 'Jane', 'Freddy']
#
# while names:
#     popped_name = names.pop()
#     if popped_name == 'Jane':
#         continue
#     print(popped_name)
#
# print('Game Over')


import sys

for arg in sys.argv:
    print('Cmd line argument:', arg)

