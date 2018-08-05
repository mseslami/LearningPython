def a(mystring, k):
    a=((int)(len(mystring) / k))
    tarray=[]
    for i in range(a):
        tarray.append(mystring[i*k:i*k+k])
        temp =""
        for j in mystring[i*k:i*k+k]:
            if j not in temp:
                temp += j

        tarray[i] =temp
    for i in tarray:
        print(i)



if __name__ == '__main__':
    a("dhdioooee",3)