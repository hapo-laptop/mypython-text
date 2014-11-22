def mplus(a,b):
    c=a
    if type(a[0])==int:
        for i in range(len(c)):
            c[i]=c[i]+b[i]
    else:
        for i in range(len(c)):
            for j in range(len(c[i])):
                c[i][j]=c[i][j]+b[i][j]
    return c

def ismatrix(a):
    if type(a[0])==int:
        for i in range(1,len(a)):
            if not type(a[i])==int:
                return False
        return True
    else:
        for i in range(1,len(a)):
            if not len(a[i])==len(a[0]):
                return False
        return True

def isequal(a,b):
    if type(a[0])==type(b[0]):
        if len(a)==len(b):
            if type(a[0])==int:
                return True
            elif len(a[0])==len(b[0]):
                return True
            else:
                return False
    else:
        return False
def madd(a,b):
    if ismatrix(a) and ismatrix(b) and isequal(a,b):
        return mplus(a,b)
    else:
        print 'there are some errors in input'.title()
