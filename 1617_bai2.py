file_open = open('1617_bai2.inp.txt', mode = 'r')
n = int(file_open.readline())
data1 = file_open.readline().split()
a=[]
for i in data1:
    a= a +[float(i)]
data2= file_open.readline().split()
b = []
for i in data2:
    b = b+ [float(i)]
file_open.close()
file_write = open('1617_bai2.out.txt', mode = 'w')
min_tg = a[1]
pos_tg = 1
min_gia = b[1]
pos_gia = 1
for i in range(n):
    if a[i]<min_tg:
        min_tg = a[i]
        pos_tg =i
    if b[i]<min_gia:
        min_gia = b[i]
        pos_gia = i
if pos_gia == pos_tg:
    file_write.write(str(pos_gia))
else:
    chenhlech = b[pos_tg] - b[pos_gia]
    phantram = chenhlech/b[pos_gia]*100
    if phantram <=10:
        file_write.write(str(pos_tg))
    else:
        file_write.write('0 co')
file_write.close()