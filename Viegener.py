def viegener(stroka, key, language, flag):
    if (language == 'RU'):
        alphabetU = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        alphabetL = alphabetU.lower()
        size = 33
    else:
        alphabetU = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        alphabetL = alphabetU.lower()
        size = 26
    array = stroka.split()
    length = len(key)
    for index, word in enumerate(array):
        key2 = (key * (len(word) // length) + key[0:len(word) % length]).upper()
        word2 = ''
        for index2, letter in enumerate(word):
            step = flag * alphabetU.find(key2[index2])
            if letter in alphabetU:
                word2 += alphabetU[(alphabetU.find(letter) + step) % size]
            elif letter in alphabetL:
                word2 += alphabetL[(alphabetL.find(letter) + step) % size]
            else:
                word2 += letter
        array[index] = word2
    return ' '.join(array)
