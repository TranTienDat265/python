import random
length = 16
password = ''
upcase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"
numb = "0123456789"
spec = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
spec = spec +'"'
password = ''
for i in range(length):
    number = random.randint(1,4)
    if (number ==1):
        rand = random.randint(0,len(upcase)-1)
        password = password + upcase[rand]
    elif (number ==2):
        rand = random.randint(0,len(lowercase)-1)
        password = password + lowercase[rand]
    elif (number == 3):
        rand = random.randint(0, len(numb)-1)
        password = password + numb[rand]
    elif (number == 4):
        rand = random.randint(0, len(spec)-1)
        password = password + spec[rand]
print(password)
