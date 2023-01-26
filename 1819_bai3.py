a = ["096","097","098","032","033","034","035","036","037","038","039"]
b = []
n = int(input("Nhập n:  "))
for i in range(n):
    b = b + [input("Nhập A[%d]: " %(i))]
for i in range(n):
    string = b[i][None:3]
    if string in a: 
        print(b[i])
    
    