a=float(input('haqiqiy sonni kiriting: '))
b=round(a,2)
print('Yuzdan birlar xonasigacha yaxlitlangan son: ',b)

a=int(input('Birinchi sonni kiriting: '))
b=int(input('Ikkinchi sonni kiriting: '))
c=int(input('Uchinchi sonnni kiriting: '))
x=max(a,b,c)
y=min(a,b,c)
print(f"Sonlarning eng kattasi: {x} Sonlarning eng kichigi: {y}")

a=float(input('Kilometrni kiriting: '))
metr=a*1000
santimetr=a*1e5
print(f"{a}km ={metr} m    {a}km={santimetr} sm")

a=int(input('Birinchi sonni kiriting: '))
b=int(input('Ikkinchi sonni kiriting: '))
x=a//b
y=a%b
print(f"Butun bo'lish {x}  Qoldiq{y}")

C=int(input('Selsiy haroratini kiriting: '))
F=(9/5)*C+32
print(f"Farangeytdagi qiymati: {F}")

a=int(input('Sonni kiriting: '))
b=a%10
print("Sonning oxirgi raqami: ",b)

a=int(input('Sonni kiriting: '))
if a%2==0:
    print('Son juft')
else:
    print('Son toq')

ism=input('Isminggizni kiriting: ')
yil=int(input("Tug'ilgan yilingizni kiriting: "))
yosh=2024-yil
print('Salom',ism,'Sizning yoshinggiz:',yosh)

a=input('Satrni kiriting:')
x=len(a)
y=a.upper()
z=a.lower()
print(f"uzunligi {x},katta: {y}, kichik: {z}")

a=input('Satrni kiriting:')
b=a[::-1]
if a==b:
    print('polindrom')
else:
    print('polindrom emas')


a=input('Satrni kiriting:')
b=len(a)
a=a.lower()
k=0
for i in a:
    if i in ["a","e","i","u","o"]:
        k+=1
print('Unlilar soni: ',k)
q=b-k
print('Undoshlar soni: ',q)


a=input('Satrni kiriting:')
b=a[::-1]
print('Teskarisi: ',b)


a=input('Berilgan gapni kiriting:')
k=len(a.split())
print(k)



a=input('Satrni kiriting:')
for i in a:
    if i.isdigit():
        print('Ha')
    else:
        print('raqam mavjud emas')