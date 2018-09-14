# how open a url in python (urllib2), request.get , re
# python is single thred
import datetime


class Contactlist(list):

    def searchname(self, name):
        searchlist = list()
        for item in self:
            if (item._std__name == name):
                searchlist.append(item._std__name)
        return searchlist


class std():
    # it's acceddable if you make an object or not

    all_membrs = Contactlist()

    def __init__(self, name, family):
        self.__name = name
        self.__family = family
        std.all_membrs.append(self)


maryam = std("maryam", "e")
# print(maryam.__name)
# print(maryam.__family)
saeed = std("saeed", "gh")
for member in std.all_membrs:
    print(member._std__name)


class supplier(std):
    def order(self, order):
        print("something".format(order, self.__name))


print(std.all_membrs.searchname("maryam"))


class friend(std):
    def __init__(self, name, family, phone):
        super().__init__(name, family)
        self.phone = phone


myfriend = friend("m", "b", 9999)
print(myfriend.phone)


# nlp, google translate, audio:
# interface is a protocol.
# if we can have multy inharitence, we don't have interface
# if we have interface, be don't have multy inharitence

class imath:
    def sum(self, a, b):
        # raise ("is not added")
        return a + b


class nm(imath):
    def sum2(self, c):
        print("a")


a = nm

# which database and why

print(a.sum(5, 5, 7))
print(a.sum2(8, 5))


# in static method we don't have eny given arg:

class Date:
    def __init__(self, year=0, month=0, day=0):
        self.year = year
        self.month = month
        self.day = day

    @staticmethod
    def d():
        dt = datetime.datetime.now()
        return Date(dt.year, dt.month, dt.day)

    def p(self):
        print(self.year, "-", self.month, "_", self.day)


mydate = Date(2015, 4, 4)
mydate.p()
print(mydate.d().year)
mydate.p()


# class method(has cls as input), static method(not any access to class variables), instance method

class person():
    __slots__ = ("name", "email", "phone")

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


someone = person("maryam", "maryam@gmail.com", 000000)
print(dir(someone))
# print(someone.__dict__)
# print(vars(someone))
# if we want to use slots we can not use dict or vars anymore
print(someone.__slots__)
def mul(x,y):
    counter =0
    if y==1:
        return x
    return x-mul(x,y-1)

print(mul(15,3))


def a (x,y):
    if x<y:
        return 0

    return 1+a(x-y,y)
print(a (15,3))