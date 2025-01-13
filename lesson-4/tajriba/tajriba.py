'''
a=11
b=1 if a%2==0 else 2    #Bir qatorlik if else elif bolmaydi
print(b)

numbers=[1,23,34,45,5,6,7,4]
a_square=[[num,num**2,num*2] for num in numbers if num%2==0]
print(a_square)


numbers=[1,23,34,45,5,6,7,4]
a_square=[print(num) for num in numbers if num%2==0]
print(a_square)

numbers=[1,23,34,45,5,6,7,4]
a_square=['a' if not print(num) else 0 for num in numbers if num%2==0] 
print(a_square)    #expression ichida bir qator ifoda bolishi kk


for i in range(3):
    for j in range(3):
        print('i=',i,'j=',j)


matrix=[[1,2,3],[4,5,6],[7,8,9]]          #matrixs=[i for i in matrix]
number=[i for num in matrix for i in num] #birinchi katta list icidan kichik loistlarni song ularni ichidan elementlarini ajratib olamiz
print(number,'matrix ichidagi raqamlar')

matrix=[[1,2,3],[4,5,6],[7,8,9]]  
number=[]
for num in matrix:
    for i in num:
        number.append(i)
        
print(number)






#dictenoary comprehensions

keys=['a','b','c','d','e']
values=[1,2,3,4,5]
d={}
for i in range(len(keys)):
    d[keys[i]]=values[i]
print(d)


keys=['a','b','c','d','e']
values=[1,2,3,4,5]
d={}
for key,val in zip(keys,values):          #zip orqali ikkita royxat ichidan chaqirib olish mumkin 
    d[key]=val
print(d)

matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]
]
matrix_square={pos:{num:num**2 for num in row} for pos,row in enumerate(matrix)}
print(matrix_square)

keys=['a','b','c','d','e']
values=[1,2,3,4,5]

d={k:v for k,v in zip(keys,values)}
print(d)


#GENERATOR EXPRESSIONS
print('GENERATOR EXPRESSIONS')


a=(num**2 for num in range(4))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
'''
#FUNKSIYA
print('FUNKSIYA')

def welcome():
    print("hello")


welcome()


def daraja(a,b):
    return a**b
c=daraja(2,3)
print('2 ning kubi- ',c)

def tanishuv(name,surname):
    print(f'Salom {name} {surname}')

tanishuv('Vasila','Shukurullayeva')   #1-tur faqat positional argument

def tanishuv(name,surname):
    print(f'Salom {name} {surname}')

tanishuv(name='Vasila',surname='Shukurullayeva')    #faqat keyword arguments
# tanishuv(name='Vasila','Shukurullayeva') bolishi mumkin emas 
# chnki argument xossasiga kora positional argument keyword argumentdan doim oldin kelishi kk

tanishuv('Vasila',surname='Shukurullayeva')    # aralash argument
 
 # / dan oldin faqat position argument yozish mn
def f(x,/,y,z,g,h,i):
    print('Ishladi funksiya')
f(1,2,3,3,4,4)  

f(1,2,z=4,g=56,h=12,i=11)#keyworddan song positional ishlatib bolmaydi


def f(x,y,z,*,g,h,i):
    print('Ishladi funksiya')

def summa(*a):
    return sum(a)
print(summa(1,2,3,4,4,5,5))