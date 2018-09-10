# python beautiful code:code
# https://gist.github.com/0x4D31/f0b633548d8e0cfb66ee3bea6a0deff9
lista = ["a", "b", "c"]
listb = [5, 6, 7, 88]
# for i, j in lista, listb:
#     print(i, j)
# zip returns a iterartor
# hovavi algorithm
for i in zip(lista, listb):
    print(i)
# read about partial
# set default to create a new dict
# what is pyenv and virtualenv (search it)


# oop
# instance method, instance variable,


print(list((4, 5, 6,)))


class Student:
    '''
    Student( lst = [{name:"", avg:""}])
    neme : name of sutdent
    avg : sutdent's averag
    this class gets list of dicts and calucate average of student's avg.
    the avg will be calucated just one time.'''

    def __init__(self, lst=[]):
        self.lst = lst
        self.get_avg()

    def get_avg(self):
        '''get_avg()
        if input argumant is empty. or if it's called befor.
        returns an integer (avg) if it's calling for the first one or
        list is not empty or null
         '''
        if len(self.lst) != 0 and self.avg == 0:
            avg = 0
            for student in self.lst:
                avg += student["avg"]
            self.avg = avg / len(self.lst)
            return self.avg
        else:
            self.avg = 0
            return "no one found or it's called befor:("


allstus = Student()
print(allstus.avg)

# allstus = Student([{"name": "maryam", "avg": 20}, {"name": "maryam", "avg": 19}])
allstus.lst = ([{"name": "maryam", "avg": 20}, {"name": "maryam", "avg": 19}])
# unittest for testbench
print(allstus.get_avg())
print(allstus.get_avg())
# print(help(allstus.get_avg()))
print(allstus.avg)
# print(help(Student))

try:
    a = 9
except ValueError:
    pass
except IndentationError:
    pass
else:
    print(" we were in try, not in exception")

import logging
# info, warning, error


import unittest


def multiply(x, y):
    return (x * y)


# unittest example:
class TestUM(unittest.TestCase):

    def setUp(self):
        pass

    def test_numbers_3_4(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_strings_a_3(self):
        self.assertEqual(multiply('a', 3), 'aaa')

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())


if __name__ == '__main__':
    unittest.main()
