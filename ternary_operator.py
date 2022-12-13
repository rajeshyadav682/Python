a=int(input('Enter First Value'))
b=int(input('Enter Second Value'))
c=int(input('Enter Thirt Value'))
max = a if a>b else b
print('Max value is :',max)
print(f'Max value is :{max}')

# biggest three number

max=  a if a>b and a>c else b if b>c else c
print(f'Biggest value is :{max}')


