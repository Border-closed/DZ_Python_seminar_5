#Крестики нолики

#Жеребьевка
import random
num=random.randint(1,2)
print(f'По результатам жеребьевки первым ходит игрок №{num}')
print('')

#Игра
igra1=['','','']
igra2=['','','']
igra3=['','','']
for i in range (100):
    print(f'Ход игрока №{num}')
    str=int((input(f'Введите номер строки ')))
    kol=int((input(f'Введите номер столбца ')))
    if (str==1 or str==2 or str==3) and (kol==1 or kol==2 or kol==3):
        if str==1:
            if igra1[kol-1]=='':
                if num==1:
                    igra1[kol-1]='Х'
                else:
                    igra1[kol-1]='0'
            else:
                print ('Эта позиция занята')
                if num==1:
                     num=2
                else:
                    num=1
        elif str==2:
            if igra2[kol-1]=='':
                if num==1:
                    igra2[kol-1]='Х'
                else:
                    igra2[kol-1]='0'
            else:
                print ('Эта позиция занята')
                if num==1:
                     num=2
                else:
                    num=1
        else:
            if igra3[kol-1]=='':
                if num==1:
                    igra3[kol-1]='Х'
                else:
                    igra3[kol-1]='0'
            else:
                print ('Эта позиция занята')
                if num==1:
                     num=2
                else:
                    num=1
    else:
        print('Введите значения строки и столбца 1 2 или 3')
        if num==1:
            num=2
        else:
            num=1
    str=0
    kol=0
    if num==1:
        num=2
    else:
        num=1
    print('')
    print(igra1)
    print(igra2)
    print(igra3)
    print('')
    if (igra1[0]==igra1[1]==igra1[2] and igra1[0]!='') or (igra2[0]==igra2[1]==igra2[2] and igra2[0]!='') or (igra3[0]==igra3[1]==igra3[2]and igra3[0]!='') or (igra1[0]==igra2[0]==igra3[0] and igra1[0]!='') or (igra1[1]==igra2[1]==igra3[1] and igra1[1]!='') or (igra1[2]==igra2[2]==igra3[2] and igra1[2]!='') or (igra1[0]==igra2[1]==igra3[2] and igra1[0]!='')  or (igra1[2]==igra2[1]==igra3[0] and igra1[2]!='') :
        if num==1:
            num=2
        else:
            num=1
        print(f'Игрок {num} победил')
        print('')
        break
    if ('' not in igra1) and ('' not in igra2) and ('' not in igra3):
        print('НИЧЬЯ')
        print('')
        break