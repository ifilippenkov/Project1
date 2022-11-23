import PySimpleGUI as sg
import codecs
from Globals import CHOICES1, CHOICES2, SIZE1, SIZE2, TEXT, INDENT, LANGUAGES
from Cesar import cesar
from CesarDeCrypt import cesarDeCrypt
from Viegener import viegener
from Vernam import vernam


layout = [
    [sg.Text('Выберите txt файл для кодировки/декодировки сообщения либо введите текст в поле')],
    [sg.Text('Если хотите вывести дешифрованный текст в txt файл, то выберите его в окне файла вывода')],
    [sg.Text('Файл ввода'), sg.InputText(key='fileinput'), sg.FileBrowse()],
    [sg.Text('Файл вывода'), sg.InputText(key='fileoutput'), sg.FileBrowse()],
    [sg.Text('Поле'), sg.Input(key='input', size=(88, 5))],
    [sg.Text('Выберите язык сообщения')],
    [sg.Listbox(LANGUAGES, size=(4, 2), key='language', enable_events=True)],
    [sg.Text(' ' * INDENT + TEXT + ' ' * INDENT), sg.Text('Выберите метод')],
    [sg.Listbox(CHOICES1, size=(SIZE1, len(CHOICES1)), key='CHOICES1', enable_events=True),
     sg.Listbox(CHOICES2, size=(SIZE2, len(CHOICES2)), key='CHOICES2', enable_events=True)],
    [sg.Text('Введите шаг для метода Цезаря либо ключ для метода Виженера, Вернама(при дешифровке)')],
    [sg.InputText(key='step')],
    [sg.Output(size=(88, 20))],
    [sg.Submit(), sg.Exit()]
]


def pprint(array, values):
    if values['fileoutput']:
        with open(values['fileoutput'], 'w') as f:
            for stroka in array:
                f.write(stroka)
                f.write('\n')
        print('Дешифрованный текст выведен в файл')
    else:
        for stroka in array:
            print(stroka)


def output(stroka, values, language):
    # Проверяем на наличие ключа, там где он нужен
    flagvernam = CHOICES2[2] != values['CHOICES2'][0] or CHOICES1[1] == values['CHOICES1'][0]
    if not values['step'] and flagvernam and CHOICES1[2] != values['CHOICES1'][0]:
        print('Введите ключ/шаг')
        return
    step = values['step']
    if CHOICES1[0] == values['CHOICES1'][0]:
        if CHOICES2[0] == values['CHOICES2'][0]:
            step = int(step)
            pprint(('Зашифрованный текст:', cesar(stroka, step, language)), values)
        elif CHOICES2[1] == values['CHOICES2'][0]:
            pprint(('Зашифрованный текст:', viegener(stroka, step, language, 1)), values)
        else:
            stroka, key = vernam(stroka, language, 1)
            pprint(('Зашифрованный текст:', stroka, 'Ваш ключ:', key), values)
    elif CHOICES1[1] == values['CHOICES1'][0]:
        if CHOICES2[0] == values['CHOICES2'][0]:
            step = int(step)
            pprint(('Дешифрованный текст:', cesar(stroka, -step, language)), values)
        elif CHOICES2[1] == values['CHOICES2'][0]:
            pprint(('Дешифрованный текст:', viegener(stroka, step, language, -1)), values)
        else:
            pprint(('Дешифрованный текст:', vernam(stroka, language, -1, step)), values)
    else:
        if CHOICES2[0] == values['CHOICES2'][0]:
            pprint(('Дешифрованный текст:', cesarDeCrypt(stroka, language)), values)
        else:
            print('Метод дешифрования без ключа работает только для метода Цезаря!')


def shifr():
    window = sg.Window('Шифровальщик', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Submit':
            if values['CHOICES1'] and values['CHOICES2'] and values['language']:
                language = values['language'][0]
                if values['fileinput'] and values['input']:
                    print('Выберите один режим ввода')
                elif values['input']:
                    stroka = values['input']
                    output(stroka, values, language)
                elif values['fileinput']:
                    stroka = ''
                    with codecs.open(values['fileinput'], encoding='utf-8') as f:
                        for value in f:
                            stroka += value
                    output(stroka, values, language)
                else:
                    print('Выберите режим ввода')
            else:
                print('Выберите режим работы, метод, язык')
    window.close()
