# https://www.hackerrank.com/challenges/merge-the-tools/problem
def a(mystring, k):
    a = ((int)(len(mystring) / k))
    tarray = []
    for i in range(a):
        tarray.append(mystring[i * k:i * k + k])
        temp = ""
        for j in mystring[i * k:i * k + k]:
            if j not in temp:
                temp += j

        tarray[i] = temp
    for i in tarray:
        print(i)

# https://www.hackerrank.com/challenges/python-string-formatting/problem:
def b(n):
    width = len("{0:b}".format(n))
    for i in range(1, n + 1):
        print(("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}").format(i, width=width))


if __name__ == '__main__':
    a("dhdioooee", 3)
    b(17)
