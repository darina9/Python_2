a= int(input('введите число'))
sum=0
for n in range(1,a+1):
    b=(1+1/n)**n
    sum+=b
    n+=1
print(f'сумма равна = {sum:.2f}')