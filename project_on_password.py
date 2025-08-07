import random
latters= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm',
          'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
          'A','B','C','D','E','F','G','H','I','J','K','L','M','N',
          'O','P','Q','R','S','T','U','V','W','X','Y','Z']
number=['0','1','2','3','4','5','6','7','8','9']
symbols=['@','#','$','&','(',')','*']

print('welcom to password generator!')
n_letters=int(input("how many latters you want in password "))
n_number=int(input("how many number you want in numbers "))
n_symbols=int(input("how many symbols you in your password "))
password=''

for i in range(1,n_letters+1):
     chare=random.choice(latters)
     password +=chare

for i in range(1,n_number):
     chare=random.choice(number)
     password +=chare

for i in range(1,n_symbols):
     chare=random.choice(symbols)
     password +=chare

print(password)
#random.shuffle(password)



