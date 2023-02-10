#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

print('-' * len(Belgium))

print(Belgium.replace(',', ':'))

Belgium_list = Belgium.split(',')
print('Population of Belgium: ', Belgium_list[1], '; Population of Brussels:', Belgium_list[4])
