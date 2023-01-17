#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных
#Ввод WWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
#Вывод 9W3B24W1B14W

#АЛГОРИТМ СЖАТИЯ
stroka=input('Введите текст, который нужно сжать ')
stroka=stroka+'.'
chislo=[]
bukva=[]
count=0
for i in range(len(stroka)-1):
    if stroka[i]==stroka[i+1]:
        count+=1
    else:
        count+=1
        chislo.append(count)
        bukva.append(stroka[i])
        count=0
output=[]
for i in range(len(chislo)):
    output.append(f'{chislo[i]}{bukva[i]}')
print(''.join(output))

#АЛГОРИТМ РАСПАКОВКИ
stroka_1=input('Введите текст, который нужно распаковать ')
bukva_1=[]
for i in range(len(stroka_1)):
    if stroka_1[i].isalpha():
        bukva_1.append(stroka_1[i])
print(bukva_1)
chislo_1=[]
for i in range(len(stroka_1)):
    if stroka_1[i].isdigit():
        chislo_1.append(stroka_1[i])
chislo_1=[int(i) for i in chislo_1]
output_1=[]
for i in range(len(chislo_1)):
    # output_1.append(f'{bukva_1[i]}*{chislo_1[i]}')
    output_1.append(f'{bukva_1[i]}'*chislo_1[i])
print(''.join(output_1))