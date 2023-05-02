n = int(input("Nhập n:  "))
tong =0 
dem=0
while n>0:
    tong += n%10
    n= n//10
    dem +=1
if dem ==0:
    print("Giá trị nhập không hợp lê")
else:
    print("Số các chữ số là: " + str(dem))
    print("Tổng các chữ số là:  " + str(tong))
