def ngto(n):
    if (n==0) or (n==1):
        return False
    dem = 0
    for i in range(1,n+1):
        if n%i ==0:
            dem +=1
    if dem==2:
        return True
    else:
        return False
n = int(input("Nhập n:  "))
ok = True
while n>0:
    if ngto(n):
        n= n //10
    else:
        ok = False
        break
if ok==True: 
    print("Siêu nguyên tố")
else: 
    print("Không phải siêu nguyên tố")