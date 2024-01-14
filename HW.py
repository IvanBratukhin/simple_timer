size=int(input("Введите длинну списка: "))
list=[]
name=str(input("Введите имя: "))
for i in range(0,size):
	list.append(name+str(i+1))
if size<=3:
	print()
if size>3:
	print("\n".join(list[1:-1]))	
print(len(list))
print(list)