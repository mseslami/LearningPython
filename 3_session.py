# try to learn these to be a full stack developer:
# lpic1 postgresql mongodb redis neo4J djengo tornodo golang
# some databases are column base oriented db like: cassandra

# a = input()
# print("a")
# print(type(a))
# lazy loading means: shows data step by step not all items in one request slow but use less memory

a, b = ("sf", "s")
# input should be list or string or iterable object:
for index, item in enumerate(a):
    print(index, item)

#  if your int is leas than 256>> it's inmutable but if grater than
#  256>> it's mutable (returns different ids for same numbers greater than 256)

# learn git by git-scm.com
# range in python 3 is lazy loading
print(type(range(5, 6)))
# with one break, try to break out two loop (use else in break not any boolean)
# if loop done completly, else will run

# solution:
for i in range(1, 100):
    for j in range(1, 100):
        break
    else:
        continue
    break

# to get a key in dictionary try get(). response might be none or something (with no error or exception)
# try getvalue() getkeys()

# sort by date and return latest third key:
mylist = ['7-8-2006', '19-3-2009', '20-11-2002', '4-8-2017', '7-10-2006']
mydate = []
mydate_dict = {}
for item in mylist:
    day = item.split("-")[0]
    month = item.split("-")[1]
    year = item.split("-")[2]
    if len(day) == 1:
        day = "0" + day
        print("you are in adding 0 to day")
        print(day)
    if len(month) == 1:
        month = "0" + month

    mydate.append(year + month + day)
    mydate_dict[year + month + day] = item
    print("dict is here")
    print(mydate_dict)

print(mydate)
mydate.sort()
print('======================================')
print(mydate)
latesst_third_key = mydate[-3]
print(mydate_dict[latesst_third_key])


# fromkeys
# try dir(mydict) to study all methods
# sorted make a new sorted object
# zip is for matching two lists or tuple returns a tuple
# use help alot !!!
# websummit.com
#  write ducstring after a def like '''shomething''' (comment is something else)
# study about swagger


# *b is a tuple, **c is a dict
def mydef(a, *b, **c):
    pass


# How to merge two dictionaries
# in Python 3.5+
# >>> x = {'a': 1, 'b': 2}
# >>> y = {'b': 3, 'c': 4}
#
# >>> z = {**x, **y}
