#Создать текстовый файл (не программно), сохранить в нем несколько строк, 
# выполнить подсчет количества строк, количества слов в каждой строке

#file = open('data.txt', 'r')
#readFile = file.read()
#readLines = file.readlines()
#print(f'Внутри файла: \n {readFile}')
#print(f'Количество строк: {len(readLines)}')


file = open('data.txt', 'r')
readFile = file.read()
print(f'Содержимое файла: \n {readFile}')

file = open('data.txt', 'r')
readLines = file.readlines()
print(f'Количество строк в файле - {len(readLines)}')

file = open('data.txt', 'r')
readLines = file.readlines()

for i in range(len(readLines)):
    print(f'Окличество символов {i + 1} - ой строки {len(readLines[i])}')

file = open('data.txt', 'r')
fileRead = file.read()
allInfo = fileRead.split()
print(f'Общее количество слов - {len(allInfo)}')
file.close()
