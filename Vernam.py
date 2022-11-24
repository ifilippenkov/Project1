from random import randint
from Viegener import viegener


def vernam(stroka, language, flag, key=''):
    if flag == 1:
        stroka = stroka.split()
        key = []
        for index, value in enumerate(stroka):
            value2 = ''
            for i in value:
                if language == 'RU':
                    alphabetU = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
                    if i not in alphabetU and i not in alphabetU.lower():
                        value2 += i
                    else:
                        step = randint(0,32)
                        value2 += alphabetU[step]
                else:
                    alphabetU = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                    if i not in alphabetU and i not in alphabetU.lower():
                        value2 += i
                    else:
                        step = randint(0,25)
                        value2 += alphabetU[step]
            key.append(value2)
            stroka[index] = viegener(value, value2, language, 1)
        return ' '.join(stroka), ' '.join(key)
    key = key.split()
    stroka = stroka.split()
    if len(key) != len(stroka):
        return 'Ключ не верный'
    for index, value in enumerate(stroka):
        if len(value) != len(key[index]):
            return 'Ключ не верный'
        stroka[index] = viegener(value, key[index], language, -1)
    return ' '.join(stroka)
