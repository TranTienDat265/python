import math
n = input("Nhập n:  ")
i=len(n)
so = ''
dem = 0
while i!=0:
    i-=1
    if n[i]!='.':
        so=n[i]+so
        dem+=1
    else:
        break
so= int(so)
nguyen = ''
for i in range(len(n)):
    if n[i] != '.':
        nguyen= nguyen + n[i]
    else:
        break
nguyen= int(nguyen)
mu = 10**dem
print(str(nguyen*mu+so)+"/"+str(mu))
ucln = math.gcd(so,mu)
so=so//ucln
mu=mu//ucln
so = nguyen*mu+so
print(str(so)+ "/"+str(mu))