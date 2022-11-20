def cesar(stroka, step, language):
    if language == 'RU':
        alphabetU = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        alphabetL = alphabetU.lower()
        size = 33
    else:
        alphabetU = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        alphabetL = alphabetU.lower()
        size = 26
    array = stroka.split()
    for index, word in enumerate(array):
        word2 = ''
        for letter in word:
            if letter in alphabetU:
                word2 += alphabetU[(alphabetU.find(letter) + step) % size]
            elif letter in alphabetL:
                word2 += alphabetL[(alphabetL.find(letter) + step) % size]
            else:
                word2 += letter
        array[index] = word2
    return ' '.join(array)
