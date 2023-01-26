def docao(n):
    tong = 0
    while n != 0:
        tong += n%10
        n = n//10
    return tong
n = int(input("Nhập số n:  "))
a = []
for i in range(n):
    a = a+ [int(input("Nhập số A[%d]:  " %(i)))]
for i in range(n):
    print(str(docao(a[i])), end=' ')
