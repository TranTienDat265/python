s = input("Nhập s:  ")
z = len(s)
i=len(s)
while i!=0:
    i -=1
    if (s[i]==' ') or (i==0):
        for j in range(i,z):
            if s[j]!=' ':
                print(s[j], end ='')
        print(' ',end='')
        z=i



