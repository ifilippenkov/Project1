import PySimpleGUI as sg
import codecs
from Cesar import cesar
from CesarDeCrypt import cesarDeCrypt
from Viegener import viegener
from Vernam import vernam

choices1 = ('Шифрование', 'Дешифрование с ключом', 'Дешифрование без ключа(только для метода Цезаря)')
choices2 = ('Метод Цезаря', 'Метод Виженера', 'Метод Вернама')
size1 = max(len(value) for value in choices1)
size2 = max(len(value) for value in choices2) + 1
text = 'Выберите режим работы шифровальщика'
indent = max((size1 - len(text)) // 2 + 6, 0)
languages = ('RU', 'EN')
layout = [
    [sg.Text('Выберите txt файл для кодировки/декодировки сообщения либо введите текст в поле')],
    [sg.Text('Если хотите вывести дешифрованный текст в txt файл, то выберите его в окне файла вывода')],
    [sg.Text('Файл ввода'), sg.InputText(key='fileinput'), sg.FileBrowse()],
    [sg.Text('Файл вывода'), sg.InputText(key='fileoutput'), sg.FileBrowse()],
    [sg.Text('Поле'), sg.Input(key='input', size=(88, 5))],
    [sg.Text('Выберите язык сообщения')],
    [sg.Listbox(languages, size=(4, 2), key='language', enable_events=True)],
    [sg.Text(' ' * indent + text + ' ' * indent), sg.Text('Выберите метод')],
    [sg.Listbox(choices1, size=(size1, len(choices1)), key='choices1', enable_events=True),
     sg.Listbox(choices2, size=(size2, len(choices2)), key='choices2', enable_events=True)],
    [sg.Text('Введите шаг для метода Цезаря либо ключ для метода Виженера, Вернама(при дешифровке)')],
    [sg.Text('При шифровании методом Вернама и дешифровании без ключа введите любой символ')],
    [sg.InputText(key='step')],
    [sg.Output(size=(88, 20))],
    [sg.Submit(), sg.Exit()]
]
window = sg.Window('Шифровальщик', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Submit':

        def pprint(array):
            if values['fileoutput']:
                with open(values['fileoutput'], 'w') as f:
                    for stroka in array:
                        f.write(stroka)
                        f.write('\n')
                print('Дешифрованный текст выведен в файл')
            else:
                for stroka in array:
                    print(stroka)

        def output(stroka):
            step = values['step']
            if choices1[0] == values['choices1'][0]:
                if choices2[0] == values['choices2'][0]:
                    step = int(step)
                    pprint(('Зашифрованный текст:', cesar(stroka, step, language)))
                elif choices2[1] == values['choices2'][0]:
                    pprint(('Зашифрованный текст:', viegener(stroka, step, language, 1)))
                else:
                    stroka, key = vernam(stroka, language, 1)
                    pprint(('Зашифрованный текст:', stroka, 'Ваш ключ:', key))
            elif choices1[1] == values['choices1'][0]:
                if choices2[0] == values['choices2'][0]:
                    step = int(step)
                    pprint(('Дешифрованный текст:', cesar(stroka, -step, language)))
                elif choices2[1] == values['choices2'][0]:
                    pprint(('Дешифрованный текст:', viegener(stroka, step, language, -1)))
                else:
                    pprint(('Дешифрованный текст:', vernam(stroka, language, -1, step)))
            else:
                if choices2[0] == values['choices2'][0]:
                    pprint(('Дешифрованный текст:', cesarDeCrypt(stroka, language)))
                else:
                    pprint(('Метод дешифрования без ключа работает только для метода Цезаря!'))

        if values['choices1'] and values['choices2'] and values['step'] and values['language']:
            language = values['language'][0]
            if values['fileinput'] and values['input']:
                print('Выберите один режим ввода')
            elif values['input']:
                stroka = values['input']
                output(stroka)
            elif values['fileinput']:
                stroka = ''
                with codecs.open(values['fileinput'], encoding='utf-8') as f:
                    for value in f:
                        stroka += value
                output(stroka)
            else:
                print('Выберите режим ввода')
        else:
            print('Выберите режим работы, метод, язык и шаг')
window.close()
