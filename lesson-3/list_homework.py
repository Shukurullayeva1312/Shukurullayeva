#Task1
a=[1,34,33,445,5,5,6,7,45]
b=a.count(5)
print(b)

#Task2
a=[1,34,33,445,5,5,6,7,45]
b=a[0]+a[1]+a[2]+a[3]+a[4]+a[5]+a[6]+a[7]+a[8]
print(b)


#Task3
a=[1,34,33,445,5,5,6,7,45]
b=max(a)
print(b)


#Task4
a=[1,34,33,445,5,5,6,7,45]
b=min(a)
print(b)


#Task5
royxat = input("Ro'yxat elementlarini probel bilan kiriting: ").split()
element = input("Tekshiriladigan elementni kiriting: ")
if element in royxat:
    print(f"{element} ro'yxatda mavjud.")
else:
    print(f"{element} ro'yxatda mavjud emas.")


#Task6
royxat=[12,34,34,'ha']
print('Birinchi elementi: ',royxat[0])

#Task7
royxat = input("Ro'yxat elementlarini probel bilan kiriting: ").split()
print('Oxirgi elementi: ',royxat[-1])

#Task8
Asl_royxat=[1,34,33,445,5,5,6,7,45]
Yangi_royxat=[]
Yangi_royxat.append(Asl_royxat[:3])
print(Yangi_royxat)


#Task9
Asl_royxat=[1,34,33,445,5,5,6,7,45]
Yangi_royxat=Asl_royxat[::-1]
print(Yangi_royxat)

#Task10
Asl_royxat=[1,34,33,445,5,5,6,7,45]
Yangi_royxat=sorted(Asl_royxat)
print(Yangi_royxat)


