#task1
a=(12,23,34,456,66,12,12,34,34)
print(a.count(12))

#task2,3
numbers=(12,23,34,456,66,12,12,34,34)
print(f"eng kattasi: {max(numbers)} eng kichigi: {min(numbers)}")

#task4
tuple1=(12,112,13,111)
if tuple1:
    birinchi=tuple1[0]
else:
    birinchi='Tuple bosh'
print("Birinchi elementi:",birinchi)

#task6
tuple1=(12,112,13,111)
if tuple1:
    oxirgi=tuple1[-1]
else:
    oxirgi='Tuple bosh'
print("Oxirgi elementi:",oxirgi)

#task7
tuple1=(12,112,13,111)
print("Elementlari soni: ",len(tuple1))
 
#task8
tuple1=(12,2322,23,1)
list1=list(tuple1)
list2=[]
list2.append(list1[:3])
tuple2=tuple(list2)
print(tuple2)

#task5
tuple1=(12,23,12,34,45,12)
element=12
for i in tuple1:
    if i==element:
        print("Element tuple da mavjud")
    else:
        print("Element tuple da mavjud emas")
    break

#task9
tuple1=(12,23,'ad')
tuple2=(56,67,78)
yangi_tuple=tuple1+tuple2
print("Yangi tuple:",yangi_tuple)

#task10
tuple1=(12,23,'ad')
if tuple1:
    print("tuple bosh emas")
else:
    print("tuple bosh")