n = input("Nhập số n:  ")
a = ["a","b","cc","bbc","cbc","abc","bac","aac","cba"]
for i in range(len(n)):
    print(a[int(n[i])-1],end='')
print()

