#Напишите программу, удаляющую из текста все слова, содержащие "а", "б" или "в".

stroka=input('Введите текст, слова разделяются пробелом ')
stroka=stroka.lower()
massiv=stroka.split()
def fil(massiv):
    if 'а' in massiv:
        return False
    elif 'б' in massiv:
        return False
    elif 'в' in massiv:
        return False
    else:
        return True
massiv_new=list(filter(fil,massiv))
print(f'Массив без слов, содержащих "а", "б" или "в": {list(massiv_new)}')