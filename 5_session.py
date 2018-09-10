# .csv files:
import argparse
import csv

nus = [['hasan', 2, 'tehran'], ["b", 5, "shiraz"]]
with open("mycsv2.csv", mode="w", encoding='utf-8', errors='ignore') as csvfile:
    # writer = csv.reader(csvfile,delimiter=",")
    # print(help(re))
    writer = csv.writer(csvfile)
    # for item in dir(writer):
    #     print(item)
    # or writerows
    writer.writerow(nus[0])
    writer.writerow(nus[1])
    # writer.writerows(nus)

# csvfile.seek(0)
with open('mycsv2.csv') as ff:
    readCsv = csv.reader(ff, delimiter=',')
    # or read and write as dict
    for row in readCsv:
        print(row)

# functions lambda:
sq = lambda x: x ** 3
print(sq(2))

# map, filter and lanbda
# give a function to map to map it to the collection
a = map(int, ['3', '5', '6', '67'])
print(sum(a))
b = (map(str.upper, ['sss', 'uuu']))
# print(b[0]+ b[1])
# sorting by value:
di = [{"name": 'jafar', 'age': 40}, {"name": 'ajafar', 'age': 406}]
# di = sorted(di, key=lambda x: x['age'], reverse=True)
# print(di)
#
# # fibunatchi is an example of reduce
from functools import reduce

#
# a = reduce(lambda x, y: x + y, [1, 1, 2, 3, 4, 5, 6])
# print(a)
#
# a = 0;
# print(di[0]['age'])

# cc = reduce(lambda x, y: {'age': x['age'] + y['age']}, di)
# print(cc.get('age'), "here 0000")
# or:
cc = reduce(lambda x, y: (int(x['age']) + int(y['age'])), di)
print(cc, "here 00009999")

# # cc = ['a','b']
# print(cc)
# print("dddddddddddddddddddddd")
# for i in cc:
#     print(i)
# # print(b)


# //
f = lambda a, b: a if (a > b) else b
reduce(f, [47, 11, 42, 102, 13])
# 102

reduce(lambda x, y: x + y, range(1, 101))
# 5050

# //////////////////////////////////////////////////////////
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)
# Output: [-5, -4, -3, -2, -1]

from collections import namedtuple, OrderedDict, ChainMap, Counter

# Basic example
Point = namedtuple('Pommint', ['x', 'y'])
p = Point(6, 7)  # instantiate with positional or keyword arguments
print(p[0] + p[1])  # indexable like the plain tuple (11, 22)
# 33
x, y = p  # unpack like a regular tuple
print(x, y)
# (11, 22)
print(p.x + p.y)
# fields also accessible by name
# 33
print(p)  # readable __repr__ with a name=value style
# Point(x=11, y=22)


EmployeeRecord = namedtuple('EmployeeRecord', 'name, age, title, department, paygrade')

employeelist = [["hasan", 40, "title1", "math", 400], ["hasan2", 40, "title1", "math", 400]
    , ["hasan3", 40, "title1", "math", 400], ["hasan4", 40, "title1", "math", 400]]
with open("employee.csv", mode='w', encoding="utf-8", errors='ignore') as file:
    writer = csv.writer(file)
    writer.writerows(employeelist)

import csv

for emp in map(EmployeeRecord._make, csv.reader(open("employee.csv", "r"))):
    print(emp.name, emp.title)

from collections import deque

d = deque('ghi')  # make a new deque with three items
for elem in d:  # iterate over the deque's elements
    print(elem.upper())

# G
# H
# I

d.append('j')  # add a new entry to the right side
# >>> d.appendleft('f')                # add a new entry to the left side
# >>> d                                # show the representation of the deque
# deque(['f', 'g', 'h', 'i', 'j'])
#
# >>> d.pop()                          # return and remove the rightmost item
# 'j'
# >>> d.popleft()                      # return and remove the leftmost item
# 'f'
# >>> list(d)                          # list the contents of the deque
# ['g', 'h', 'i']
# >>> d[0]                             # peek at leftmost item
# 'g'
# >>> d[-1]                            # peek at rightmost item
# 'i'
#
# >>> list(reversed(d))                # list the contents of a deque in reverse
# ['i', 'h', 'g']
# >>> 'h' in d                         # search the deque
# True
# >>> d.extend('jkl')                  # add multiple elements at once
# >>> d
# deque(['g', 'h', 'i', 'j', 'k', 'l'])
# >>> d.rotate(1)                      # right rotation
# >>> d
# deque(['l', 'g', 'h', 'i', 'j', 'k'])
# >>> d.rotate(-1)                     # left rotation
# >>> d
# deque(['g', 'h', 'i', 'j', 'k', 'l'])
#
# >>> deque(reversed(d))               # make a new deque in reverse order
# deque(['l', 'k', 'j', 'i', 'h', 'g'])
# >>> d.clear()                        # empty the deque
# >>> d.pop()                          # cannot pop from an empty deque
# Traceback (most recent call last):
#     File "<pyshell#6>", line 1, in -toplevel-
#         d.pop()
# IndexError: pop from an empty deque
#
# >>> d.extendleft('abc')              # extendleft() reverses the input order
# >>> d
# deque(['c', 'b', 'a'])

# in baraye zamani hast ke agar key hatoon barabar bood
# che action i anjam bedin
from collections import defaultdict

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)
    # print(k, v)

print(sorted(d.items()), "dddddddddddddddddddddddd")

# [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]


d = OrderedDict.fromkeys('abcde')
d.move_to_end('b')
print(d)
print(''.join(d.keys()))
# 'acdeb'
d.move_to_end('b', last=False)
print(d)

# #  -----------------
# sort by key, value and len:
# regular unsorted dictionary
d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
# dictionary sorted by key
OrderedDict(sorted(d.items(), key=lambda t: t[0]))
# OrderedDict([('apple', 4), ('banana', 3), ('orange', 2), ('pear', 1)])
#
# dictionary sorted by value
OrderedDict(sorted(d.items(), key=lambda t: t[1]))
# OrderedDict([('pear', 1), ('orange', 2), ('banana', 3), ('apple', 4)])
#
# dictionary sorted by length of the key string
OrderedDict(sorted(d.items(), key=lambda t: len(t[0])))
# OrderedDict([('pear', 1), ('apple', 4), ('orange', 2), ('banana', 3)])


# import os, argparse
# defaults = {'color': 'red', 'user': 'guest'}
# parser = argparse.ArgumentParser()
# parser.add_argument('-u', '--user')
# parser.add_argument('-c', '--color')
# print(parser)
# namespace = parser.parse_args()
# print(namespace)
# command_line_args = {k:v for k, v in vars(namespace).items() if v}
# print(command_line_args)
#
# combined = ChainMap(command_line_args, os.environ, defaults)
# print(combined['color'])
# print(combined['user'])


c = Counter()  # a new, empty counter
print(c)
c = Counter('gallahad')  # a new counter from an iterable
print(c)
c = Counter({'red': 4, 'blue': 2})  # a new counter from a mapping
print(c)
c = Counter(cats=4, dogs=8)  # a new counter from keyword args
print(c)
# https://docs.python.org/3/library/collections.html#collections.Counter


# 1/2/2014,5,8,red
# 1/3/2014,5,2,green
# 1/4/2014,9,1,blue
#
# ----------------------
#
# import csv
#
# with open('example.csv') as csvfile:
#     readCSV = csv.reader(csvfile, delimiter=',')
#     for row in readCSV:
#         print(row)
#         print(row[0])
#         print(row[0],row[1],row[2],)
#
# #DictReader
# import csv
# f = open('values.csv', 'r')
# with f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         print(row['min'], row['avg'], row['max'])
#
# -----------------------
# import csv
# nms = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]]
# f = open('numbers2.csv', 'w')
# with f:
#     writer = csv.writer(f)
#     for row in nms:
#         writer.writerow(row)
#
#
# import csv
# nms = [[1, 2, 3], [7, 8, 9], [10, 11, 12]]
# f = open('numbers3.csv', 'w')
# with f:
#     writer = csv.writer(f)
#     writer.writerows(nms)
#
#
# import csv
# f = open('names.csv', 'w')
# with f:
#     fnames = ['first_name', 'last_name']
#     writer = csv.DictWriter(f, fieldnames=fnames)
#     writer.writeheader()
#     writer.writerow({'first_name' : 'John', 'last_name': 'Smith'})
#     writer.writerow({'first_name' : 'Robert', 'last_name': 'Brown'})
#     writer.writerow({'first_name' : 'Julia', 'last_name': 'Griffin'})
#
# import csv
# csv.register_dialect("hashes", delimiter="#")
# f = open('items3.csv', 'w')
# with f:
#     writer = csv.writer(f, dialect="hashes")
#     writer.writerow(("pens", 4))
#     writer.writerow(("plates", 2))
#     writer.writerow(("bottles", 4))
#     writer.writerow(("cups", 1))
