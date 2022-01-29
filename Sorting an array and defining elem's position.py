#Далее программа работает по следующему алгоритму:
#Преобразование введённой последовательности в список
#Сортировка списка по возрастанию элементов в нем (для реализации сортировки определите функцию)
#Устанавливается номер позиции элемента, который меньше введенного пользователем числа, а следующий за ним больше или равен этому числу.
try:
    array=list(map(int,input("enter any numbers with a space in between:\n").split()))

    def sort_array ():
        for i in range(len(array)):
           for j in range(len(array) - i - 1):
               if array[j] > array[j + 1]:
                   array[j], array[j + 1] = array[j + 1], array[j]
        return array
    print(sort_array())
    num=int(input("enter some number:\n"))
    sort=sort_array()

    def count(sort, elem):
        count = 0
        for a in sort:
            if a == elem:
                count += 1
        return count

    minimum=min(sort)
    maximum=max(sort)
    def num_position (sort, elem, left, right):
            if left > right: # если левая граница превысила правую,
                return 'entered number is not stated in the array, pleas try again'  # значит элемент отсутствует
            middle = (right+left) // 2 # находимо середину
            if elem < minimum: #если элемент меньше минимального значения последовательности,
               return 'entered number is lower than minimal value in the array' # индекс предыдущего значения, таким образом, не существует
            elif elem == minimum:  #если элемент равен минимальному значению
               return 'entered number is equal to the minimal position of the array' # индекс предыдущего значения, таким образом, не существует
            elif elem > maximum:  #если элемент больше максимального значения
               return 'entered number is bigger than maximal value in the array'
            if sort[middle] == elem: # если элемент в середине,
                return middle # возвращаем этот индекс
            elif elem < sort[middle]: # если элемент меньше элемента в середине
                 return num_position(sort, elem, left, middle-1) # рекурсивно ищем в левой половине
            else: # иначе в правой
                return num_position(sort, elem, middle+1, right)

    print(num_position(sort, num, 0, len(sort))) # запускаем алгоритм на левой и правой границе

except ValueError or NameError as error:  # возвращаю сообщение ниже, если число не включено в массив
    print( "Please enter a valid numeric array")
