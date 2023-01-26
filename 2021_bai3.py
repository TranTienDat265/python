n = int(input("Nhập n:  "))
s=''
while n !=0:
    so= n %2
    n= n//2
    s=str(so)+s
print(s)