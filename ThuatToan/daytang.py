n = int(input("Nhập n:  "))
a = []
for i in range(n):
    a = a +[int(input("Nhập A[%d]:  " %(i) ))]
dem = 0
for i in range(n-1):
    if a[i] <= a[i+1]:
        dem +=1
if dem==n-1:
    print("Dãy tăng")