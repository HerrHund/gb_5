# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. 
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

def summary():
    try:
        with open('sum.txt', 'w+') as f:
            numbs = input('Введите числа через пробел \n')
            f.writelines(numbs + ' числа которые Вы ввели \n')
            myNumbs = numbs.split()
            suumma = sum(map(int, myNumbs))
            f.writelines(str(f'{suumma} а это сумма этих чисел'))

            

            print(sum(map(int, myNumbs)))
    except IOError:
        print('Error IO')
    except ValueError:
        print('Error Value')
summary() 
