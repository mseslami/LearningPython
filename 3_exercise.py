# 1. Write a Python script to sort (ascending and descending) a dictionary by value:
import operator

x = {1: "e", 3: "d", 4: "c", 2: "d", 0: "s"}
sortedx = sorted(x.items(), key=operator.itemgetter(1))  # sorted by value
sortedx2 = sorted(x.items(), key=operator.itemgetter(0))  # sorted by key
print(sortedx)
print(sortedx2)

# 2. Write a Python script to add a key to a dictionary:
a = {0: 10, 1: 20}
a[2] = 30
# or:
# a.update({2:30})
print(a)

# 3. Write a Python script to concatenate following dictionaries to create a new one:
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
finaldict = dic1.copy()
finaldict.update(dic2)
finaldict.update(dic3)
print(finaldict)

# 4. Write a Python script to check if a given key already exists in a dictionary:
givenkey = 2
dic1 = {1: 10, 2: 20}
for i in dic1.keys():
    if i == givenkey:
        print("given key is found!")
        break

# 5. Write a Python program to iterate over dictionaries using for loops:
dic1 = {1: 10, 2: 20}
for i, j in dic1.items():
    print(i, j)

# 6.Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x):
n = 5
dic1 = {}
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
for i in range(1, n + 1):
    dic1.update({i: i * i})
print(dic1)

# 7. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys:
dic1 = {}
for i in range(1, 16):
    dic1.update({i: i * i})
print(dic1)

# 8. Write a Python script to merge two Python dictionaries:
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
finaldict = dic1.copy()
finaldict.update(dic2)
print(finaldict)

# 9. Write a Python program to iterate over dictionaries using for loops:
dic1 = {1: 10, 2: 20}
for i, j in dic1.items():
    print(i, j)

# 10. Write a Python program to sum all the items in a dictionary:
dic1 = {1: 10, 2: 20}
sum = 0
for i in dic1.values():
    sum += i
# or:
# print(sum(my_dict.values()))
print(sum)

# 11. Write a Python program to multiply all the items in a dictionary:
dic1 = {1: 10, 2: 20}
sum = 1
for i in dic1.values():
    sum *= i
print(sum)

# 12. Write a Python program to remove a key from a dictionary:
dic1 = {1: 10, 2: 20}
dic1.pop(1)
# or:
# del dic1[2]
print(dic1)

# 13. Write a Python program to map two lists into a dictionary:
keylist = [1, 2]
valuelist = [10, 20]
zipeddict = dict(zip(keylist, valuelist))
print(zipeddict)

# 14. Write a Python program to sort a dictionary by key:
dic1 = {2: 3, 1: 20}
dic1 = sorted(dic1.items())
print(dic1)

# 15. Write a Python program to get the maximum and minimum value in a dictionary:
dic1 = {2: 3, 1: 20}
maxvalu = max(dic1.values())
minvalu = min(dic1.values())
print(maxvalu, minvalu)


# 16.Write a Python program to get a dictionary from an object's fields:
class testclass():
    def __init__(self):
        self.a = 5
        self.b = 9


sample = testclass()
print(sample.__dict__)

# 17. Write a Python program to remove duplicates from Dictionary:
dic1 = {7: 3, 5: 3, 2: 3, 1: 20}
dic2 = {}
for i, j in dic1.items():
    if j not in dic2.values():
        dic2.update({i: j})
print(dic2)

# 18. Write a Python program to check a dictionary is empty or not:
dic1 = {}
if len(dic1) == 0:
    print("it's empty :(")
# or:
# if not bool(dic1):
#     print("it's empty :(")


# 19. Write a Python program to combine two dictionary adding values for common keys:
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
d3 = d1.copy()
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
for i, j in d2.items():
    if i not in d3.keys():
        d3.update({i: j})
    else:
        d3.update({i: j + d3.get(i)})
print(d3)
# or:
# 20. Write a Python program to print all unique values in a dictionary:
dic1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

listtoprint = set(val for dic1 in dic1 for val in dic1.values())
print(listtoprint)

# 21. Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary:
print("see here")
a = ""
dic1 = {'1': ['a', 'b'], '2': ['c', 'd']}
for i, j in dic1.items():
    for y in range(0, len(j)):
        sum = j[y]
        for w, u in dic1.items():
            if w > i:
                for e in range(0, len(u)):
                    sum = j[y]
                    sum += str(u[e])
                    a += sum + "\n"
print(a)

# or:
# import itertools
# d = {'1': ['a', 'b'], '2': ['c', 'd']}
# for combo in itertools.product(*[d[k] for k in sorted(d.keys())]):
#     print(''.join(combo))


# 22. Write a Python program to find the highest 3 values in a dictionary:
d1 = {'a': 100, 'b': 200, 'c': 300, 'aa': 1050, 'ba': 2050, 'ca': 3050}
listtoprint = []
for i in range(0, 3):
    listtoprint.append(max(d1.values()))
    d1.pop(max(d1))
print(listtoprint)
# or:
# from heapq import nlargest
# three_largest = nlargest(3, d1, key=d1.get)
# print(three_largest)


# 23. Write a Python program to combine values in python list of dictionaries:
a = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# Expected Output: Counter({'item1': 1150, 'item2': 300})
from collections import Counter

result = Counter()
for i in a:
    result[i["item"]] += i["amount"]
print(result)

# 24. Write a Python program to create a dictionary from a string:
mystring = 'w3resource'
dic1 = {}
for i in mystring:
    if i not in dic1.keys():
        dic1.update({i: 1})
    else:
        dic1.update({i: dic1.get(i) + 1})
print(dic1)

# 25. Write a Python program to print a dictionary in table format:
dic1 = {'a': 100, 'b': 200, 'c': 300, 'aa': 1050, 'ba': 2050, 'ca': 3050}
rows = ""
cols = ""
for i, j in dic1.items():
    temp = "{:<10}".format(i)
    rows += temp
for i, j in dic1.items():
    temp = "{:<10}".format(j)
    cols += temp
print(rows)
print(cols)

# or:
# for row in zip(*([key] + (value) for key, value in sorted(dic1.items()))):
#     print(*row)


# 26. Write a Python program to count the values associated with key in a dictionary:
mylist = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'},
          {'id': 3, 'success': True, 'name': 'Alex'}]
# Expected result: Count of how many dictionaries have success as True
counter = 0
for i in mylist:
    if i["success"] == True:
        counter += 1
print(counter)
# or:
# print(sum(i['success'] for i in mylist))


# 27. Write a Python program to convert a list into a nested dictionary of keys:
mylist = ["a", "b", "c", "d"]
new_dict = current = {}
for name in mylist:
    current[name] = {}
    current = current[name]
print(new_dict)

# 28. Write a Python program to sort a list alphabetically in a dictionary:
dic1 = {0: "c", 1: "y", 2: "i", 3: "x"}
print(sorted(dic1.items(), key=operator.itemgetter(1)))

# 29. Write a Python program to remove spaces from dictionary keys:
dic1 = {0: "  c  ", 1: " y ", 2: " i ", 3: " x    "}
for j, i in dic1.items():
    dic1.update({j: i.replace(" ", "")})
print(dic1)

# 30. Write a Python program to get the top three items in a shop:
dic1 = {'item1': 45.50, 'item2': 35, 'item3': 41.30, 'item4': 55, 'item5': 24}
from heapq import nlargest

print(nlargest(3, dic1.items(), key=operator.itemgetter(1)))

# 31. Write a Python program to get the key, value and item in a dictionary:
dic1 = {'item1': 45.50, 'item2': 35, 'item3': 41.30, 'item4': 55, 'item5': 24}
counter = 0
for i, j in dic1.items():
    temp = "{:<10}".format(i)
    print("{:<10}{:<10}{:<10}".format(i, j, counter))
    counter += 1
# or:
# for count, (key, value) in enumerate(dic1.items(), 1):
#     print(key,'   ',value,'    ', count)


# 32. Write a Python program to print a dictionary line by line:
dic1 = {'item1': 45.50, 'item2': 35, 'item3': 41.30, 'item4': 55, 'item5': 24}
for i in dic1.items():
    print(i)
# or:
# students = {'Aex':{'class':'V',
#         'rolld_id':2},
#         'Puja':{'class':'V',
#         'roll_id':3}}
# for a in students:
#     print(a)
#     for b in students[a]:
#         print (b,':',students[a][b])


# 33. Write a Python program to check multiple keys exists in a dictionary:
dic1 = {'item1': 45.50, 'item2': 35, 'item3': 41.30, 'item4': 55, 'item5': 24}
if all(k in dic1 for k in ("item1", "item2")):
    print("True")
# or:
# print(dic1.keys()>={"item1","item2"})


# 34. Write a Python program to count number of items in a dictionary value that is a list:
dic1 = {'1': ['a', 'b'], '2': ['c', 'd']}
counter = 0
for i in dic1.values():
    counter += len(i)
print(counter)
# or:
# ctr = sum(map(len, dic1.values()))
# print(ctr)


# 35. Write a Python program to sort Counter by value:
dic1 = {'Math': 81, 'Physics': 83, 'Chemistry': 87}
print(sorted(dic1.items(), key=operator.itemgetter(1))[::-1])
# or:
# from collections import Counter
# x = Counter(dic1)
# print(x.most_common())


# 36. Write a Python program to create a dictionary from two lists without losing duplicate values:
mylist = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
indexlist = [1, 2, 2, 3]
print(dict(zip(mylist, indexlist)))

# 37. Write a Python program to replace dictionary values with their sum:
dic1 = {'1': ['a', 'b'], '2': ['c', 'd']}
for i, j in dic1.items():
    sum = ""
    for y in range(0, len(j)):
        sum += j[y]
    dic1.update({i: sum})
print(dic1)

# 38. Write a Python program to match key values in two dictionaries:
dic1 = {'key1': 1, 'key2': 3, 'key3': 2}
dic2 = {'key1': 1, 'key2': 2}
for i, j in dic1.items():
    for y, u in dic2.items():
        if i == y:
            print("same key in both dicts is: ", i)
            break
    else:
        continue
    break


#fix it:
print("=====================================")
x = {1: "e", 3: "d", 4: "c", 2: "d", 0: "s"}
# sortedx = sorted(x.items(), key=operator.itemgetter(1))  # sorted by value
# sortedx.sorted()
# sortedx = sorted(x.items())  # sorted by value
a = list(x.values())
# print(a)
n = len(a)
while n:
    for i in range(n - 1):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
    n -= 1

print(a)
# dict = {'Neetu':22,'Shiny':21,'Poonam':23}
# sorted(x.items())

# print(sorted(x.values()))
# print sv
