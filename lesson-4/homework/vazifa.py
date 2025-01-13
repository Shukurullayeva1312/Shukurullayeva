#task1
royxat1=[1,2,34,56,5,4,5,6]
royxat2=[1,34,45,56,2,87,95,9]
yangi_royxat=[]

for i in royxat2:
    if i not in royxat1:
        yangi_royxat.append(i)

for i in royxat1:
    if i not in royxat2:
        yangi_royxat.append(i)

print(yangi_royxat)

#Task2
n=int(input('Sonni kiriting: '))
for i in range(1,n):
    print(i**2)   



#Task3
def process_string(txt):
    result = []
    vowels = 'aeiou'

    for i, char in enumerate(txt):
        result.append(char)

        if (i + 1) % 3 == 0:
            result.append('_')

        elif char in vowels and i < len(txt) - 1:
            result.append('_')
    processed_txt = ''.join(result).rstrip('_')
    return processed_txt
print(process_string("salom"))  
print(process_string("assalom"))
print(process_string("abcabcdabcdeabcdefabcdefg"))






#task5

def check_password():
    password = input("Parolni kiriting: ")
    if len(password) < 8:
        print("Parol juda qisqa")
    elif not any(char.isupper() for char in password):
        print("Parol bosh harfdan iborat bo'lishi kerak")
    else:
        print("Parol kuchli")
check_password()

