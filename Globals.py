CHOICES1 = ('Шифрование', 'Дешифрование с ключом', 'Дешифрование без ключа(только для метода Цезаря)')
CHOICES2 = ('Метод Цезаря', 'Метод Виженера', 'Метод Вернама')
SIZE1 = max(len(value) for value in CHOICES1)
SIZE2 = max(len(value) for value in CHOICES2) + 1
TEXT = 'Выберите режим работы шифровальщика'
INDENT = max((SIZE1 - len(TEXT)) // 2 + 6, 0)
LANGUAGES = ('RU', 'EN')