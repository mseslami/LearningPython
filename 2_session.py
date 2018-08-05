name = 'saezd'
name = name.replace('r', 'b', 1)
print(name)

# rfind same as rindex
# name.rindex("a", start , end)
myindex = name.rindex("e")
# delete a charachter
print(name[:myindex] + name[myindex + 1:])
print(name[:3] + name[4:])
# if we had five e how could access to third e???? replace it

name = "saeeeeed"
name = name.index("e", 2, 4)
print(name)

name = "saeed"
name = name.zfill(20)
print(name)
name = "     sa ee  d  d   "

# strip removes extra space befor and after str:
print(name.strip())
name = name.replace(" ", "")
print(name)
help(name.split())
a = "hey hi hello"
a = a.partition("i")
print(a)
a = "hey hi i hello"
a = a.strip('i')
print(a)
print("see this a")


# main def is the last method. write it in the last part


def sum(a, b):
    return a + b


# pass in a def means don't crash until i finish the def
# try katties && hackerrank (it's professional)


def test():
    pass


if name == 'main':
    a = sum(4, 5)
    print(a)

# difference between repr & str
# import datetime
# datetime.datetime.now()...
# user eval change str to class
# read bout secuerity of eval
# format:
name = "salamnew"
a = f"salam salam salam {name}"
print(a)

# !s !r !a
# to access to eval of a string  upper code doesn't work. it's in repr , it's eval able like below:
a = f"salam salam salam {name!r}"
# print(eval(f"salam salam salam {name}".split()[3]))   error acurs
print(eval(f"salam salam salam {name!r}".split()[3]))
# how use  % to do same thing
# try dir of a object ot access to all of the functions
print("{1}  my name is {0} {1}".format("salam", "hi"))
print(eval("7+3*2"))

# eval is tooo dangrous. if user write some code to access to our files, it's terrible!!
d = dict(who="saeed", what="pizza")
from string import Template

s = Template("$who likes $what")
s.substitute(d)
print(s)
# upper code doesn't work
# list is mutable
a = [4, 5, 6, [5, 6, 7], 7]
print(a[3][1])
# some functions are inplace some aren't. replace is not. sort is.
# all list methodes are inplace
# list.pop (filo)
# a.remove(value)

a.insert(0, "saeed")
print(a)

a.insert(0, "saeed2")
print(a)

# key i dict can be jsut inmutable objects
# diffrence between extend and insert:
a.extend(["s", "d", 5])
print(a)
print(a.count("s"))

# assignment is something!  shallow copy: same reference. deep copy: totaly separated ( assign to two different things:
# list.copy() or list.deepcopy
# not sure about it!

# to remove repeatitive items :
# set(a)
# it's muteable
# print(a)
# study dir set: intersection, add to end
# tuple is like list but with (). is not extendable. is so fast. it's inside stack not in heap.  it's inmutable.
# list of a string is list of characters of a list


print('{:,}'.format(1234567777))
points = 20
total = 90
print('Correct answers: {:.2%}'.format(points / total))

for align, text in zip('<^>', ['left', 'center', 'right']):
    print('{0:{fill}{align}25}'.format(text, fill=align, align=align))

octets = [192, 168, 0, 1]
print('{:02X}{:02X}{:02X}{:02X}'.format(*octets))
# 'C0A80001'

# a = int(_, 16)
# 3232235521

width = 5
for num in range(5, 12):
    for base in 'dXob':
        print('{0:{width}{base}}'.format(num, base=base, width=width), end=' ')
    print("")

# format also supports binary numbers
print("int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42))
# 'int: 42;  hex: 2a;  oct: 52;  bin: 101010'

# with 0x, 0o, or 0b as prefix:
print("int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42))
# 'int: 42;  hex: 0x2a;  oct: 0o52;  bin: 0b101010'

print('{:<30}'.format('left aligned'))
# 'left aligned                  '
print('{:>30}'.format('right aligned'))
# '                 right aligned'
print('{:^30}'.format('centered'))
# '           centered           '
print('{:*^30}'.format('centered'))  # use '*' as a fill char
# '***********centered***********'

coord = (3, 5, 7)
print('X: {0[2]};  Y: {1}'.format(coord, 8))
# 'X: 3;  Y: 5'
