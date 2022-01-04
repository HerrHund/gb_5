#Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. 
# Об окончании ввода данных свидетельствует пустая строка.

openFile = open('data.txt', 'w')
data = input('Введите текст \n')


while data:
    openFile.writelines(data)
    data = input('Введите текст \n')
    if not data:
        break


openFile.close()
openFile = open('data.txt', 'r')


print(openFile.readlines())
openFile.close()


