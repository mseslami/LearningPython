# default end is \n default sep is space:
print('b', 'c', 'd', sep=', ', end='!!!\n')
mylist = [3, 3, 4, 5, 6, 6]
for item in mylist:
    print(item, end=",")

# read and write in file:
# read about IO in help(open) or help(print)

# flush just speed up; it dosnt' save data in buffer. turn flush on to  send data to file immediately

# in evey package we should have a __init__.py file (jump to pythontest project)
# touch in cmd means just create it. by  "cat" open .txt
# write : filename tree >> to see it's tree in cmd (search it)
# SampleProject
# .
# ├── sample_project.py
# ├── module_one.py
# └── pakage/
#     ├── __init__.py
#     ├── module_two.py
#     └── module_three.py


# open return a string file. mode: read about it,

myfile = open('/home/maryam/Documents/sample.txt', mode="+w")
myfile.writelines("df       hdkf \ndjf f")

print('\n================')
print(myfile.tell())
print(len("df     hdkf \ndjf f"))
myfile.seek(0)
print(myfile.tell())
print(myfile.read())
print(myfile.tell())
# myfile.seek(0)
print("ddddddddddddddd")
# myfile.seek(index)
myfile.writelines("hi hi hi")
myfile.seek(0, 1)
print(myfile.read())
# myfile = input("", open(('home/maryam/Documents/sample.txt'), mode="+w"))
# print(myfile)
# truncate:

# ? create a dic, save data, search by book id, writer's name, create a binary file,
#  with read and write, add , delete, edit,
# it should support CRَUD: create, update, read, delete.


# ? difference between readlines in w+ mood and r?

# ternary:
a = False
b = "saeed " if a else "reze"
print(b)
mylist = [3, 4, 5, 6]
print([x if x % 2 else x * 2 for x in mylist])

# if you don't close your file, your data wont be saved until closing:
# with this line of codes, we don't need to close it, it will be closed by
# __exit__

# with open("a.txt") as f, open("a2.txt") as f2:
#     # print(f.readline())
#     pass


mylist = [3, 3, 4, 5, 6, 7, 0]
mylist2 = [2, 1, 3]
mylist = set(mylist)
mylist2 = set(mylist2)
print({item: 'ss' for item in mylist if item % 2 == 0})
mystr = "dfjdkfjdk"
# it's a list of dicts:
newdic = [{item: item2} for item in mylist for item2 in mylist2]
print(newdic)
# just a dict:
newdic = {item: item2 for item in mylist for item2 in mylist2}
print(newdic)

mydict = {"a": "b", "c": "d"}


def dispatcher(a):
    print(dict.get(mydict, a, "else"))


dispatcher("g")

# you may need exit numbers (just search about it)

# import os
# os.getcwd()

# import sys
# sys.platform
# sys.exit()
