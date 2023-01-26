s = input("Nhập s: ")
pow =len(s)
n=0
for i in range(len(s)):
    so = int(s[i])
    pow -=1
    n = n+ (so*(2**pow))
    """ print(n)
    print(str(i)+"  "+ str(pow)) """
print(n)
