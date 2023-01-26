n = int(input("Nhập n:  "))
dem=0
tong=0
print("- Các ước của N là:", end =' ')
for i in range(1,n+1):
    if n % i == 0:
        print(i, end=' ')
        dem+=1
        tong+=i
print()
print("- N có "+ str(dem) + " ước")
print("- Tổng các ước của N là: " + str(tong)) 