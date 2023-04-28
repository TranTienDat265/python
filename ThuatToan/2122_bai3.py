def doixung(n):
    st = str(n)
    st2 = ''
    for i in range(len(st)):
        st2=st[i]+st2
    if st2 == st:
        return True
    else:
        return False
def dao(n):
    st=str(n)
    st2=''
    for i in range(len(st)):
        st2=st[i]+st2
    st2=int(st2)
    return st2
n=int(input("Nhập n:  "))
while doixung(n) != True:
    n = n + dao(n)
print(n)


