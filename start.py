import os

enterous = input('Enter name file:     ')
def finder (strip = enterous):
    list_1 = []; counter = 0
    current_dir = os.getcwd()
    items_now = os.listdir(current_dir)
    for i in items_now:
        if i == strip:
            list_1.append(i)
            counter += 1

    return ('Найденные файлы: {} ,Количество найденных файлов: {}'.format(list_1, counter))



print(finder())



