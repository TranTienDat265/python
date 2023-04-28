n = int(input("Nhập số n:  "))
s = 0
for i in range(1,n+1):
    s=s+i/(i*(i+2))
print(s)