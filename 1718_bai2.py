x = int(input("Nhập x:  "))
y = int(input("Nhập y:  "))
dem=0
for i in range(x,y):
    if (i%2 == 0) and (i%3==0):
        dem +=1
        print(i,end=' ')
if dem==0:
    print("Không có giá trị nào thỏa mãn")