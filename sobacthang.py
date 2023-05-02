def sbt(n):
    s = str(n)
    if len(s) <=1:
        return False
    dem=0
    for i in range(len(s)-1):
        so1 = int(s[i])
        so2 = int(s[i+1]) 
        if so1<so2:
            dem+=1
    if dem == len(s)-1:
        return True
    else:
        return False
file_open = open('sbt.txt', 'r')
file_write = open('sbt.out.txt', 'w')
n = int(file_open.readline())
data = file_open.readline().split()
file_open.close()
a = []
for i in data:
    a = a + [int(i)]
for i in range(n):
    if sbt(a[i]):
        file_write.write(str(a[i])+ " ")
file_write.close()
