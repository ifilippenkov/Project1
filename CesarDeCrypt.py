import codecs
from collections import Counter
from Cesar import cesar

#Выведем частотности встречаемых букв из файлов в соответсвующие словари
dictionaryRu2 = dict()
dictionaryEn2 = dict()
with codecs.open('input', encoding='utf-8') as f:
    for value in f:
        keys = (''.join(value.split(':')).split())[::2]
        values = (''.join(value.split(':')).split())[1::2]
        dictionary = dict(zip(keys, values))
        dictionaryRu2.update(dictionary)


with codecs.open('input2', encoding='utf-8') as f:
    for value in f:
        keys = (''.join(value.split(':')).split())[::2]
        values = (''.join(value.split(':')).split())[1::2]
        dictionary = dict(zip(keys, values))
        dictionaryEn2.update(dictionary)

#Впоследствие нам понадобится отсортированный по алфавиту словарь, а эти - неотсортированы
alphabetRu = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
alphabetEn = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
dictionaryRu = dict()
dictionaryEn = dict()
for keys in alphabetRu:
    dictionaryRu[keys] = float(dictionaryRu2[keys])
for keys in alphabetEn:
    dictionaryEn[keys] = float(dictionaryEn2[keys])


def cesarDeCrypt(stroka, language):
    if language == 'RU':
        alphabetU = alphabetRu
        size = 33
        array2 = list(dictionaryRu.values())
    else:
        alphabetU = alphabetEn
        size = 26
        array2 = list(dictionaryEn.values())
    #Построим словарь частотности букв данной строки
    dictionary = dict()
    for keys in alphabetU:
        dictionary[keys] = 0
    stroka2 = ''.join(stroka.split())
    length = len(stroka2)
    dictionary.update(dict(Counter(stroka2.upper())))
    #Удалим не буквы из словаря
    array3 = list()
    for keys in dictionary.keys():
        if not(keys in alphabetU):
            array3.append(keys)
    for keys in array3:
        del dictionary[keys]
    #Округлим до сотых частоты встречаемости
    for keys, values in dictionary.items():
        dictionary[keys] = round(values / length * 100, 2)
    #Найдем шаг, на который сдвинуты буквы в закодированой строке методом Цезаря методом наименьших квадратов
    array = list(dictionary.values())
    min = 100000
    step = 0
    for i in range(size):
        sum = 0
        for j in range(size):
            sum += (array2[j] - array[(i + j) % size]) ** 2
        if sum < min:
            min = sum
            step = i
    #Декодируем строку по найденому шагу
    return cesar(stroka, -step, language)
