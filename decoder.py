import re

PATH_TO_FILE = '/Users/owl/Desktop/send_contacts.vcf'

ALPHABET = {
    '=D0=B0': 'а',
    '=D0=B1': 'б',
    '=D0=B2': 'в',
    '=D0=B3': 'г',
    '=D0=B4': 'д',
    '=D0=B5': 'е',
    '=D1=91': 'ё',
    '=D0=B6': 'ж',
    '=D0=B7': 'з',
    '=D0=B8': 'и',
    '=D0=B9': 'й',
    '=D0=BA': 'к',
    '=D0=BB': 'л',
    '=D0=BC': 'м',
    '=D0=BD': 'н',
    '=D0=BE': 'о',
    '=D0=BF': 'п',
    '=D1=80': 'р',
    '=D1=81': 'с',
    '=D1=82': 'т',
    '=D1=83': 'у',
    '=D1=84': 'ф',
    '=D1=85': 'х',
    '=D1=86': 'ц',
    '=D1=87': 'ч',
    '=D1=88': 'ш',
    '=D1=89': 'щ',
    '=D1=8A': 'ъ',
    '=D1=8B': 'ы',
    '=D1=8C': 'ь',
    '=D1=8D': 'э',
    '=D1=8E': 'ю',
    '=D1=8F': 'я',

    '=D0=90': 'А',
    '=D0=91': 'Б',
    '=D0=92': 'В',
    '=D0=93': 'Г',
    '=D0=94': 'Д',
    '=D0=95': 'Е',
    '=D0=81': 'Ё',
    '=D0=96': 'Ж',
    '=D0=97': 'З',
    '=D0=98': 'И',
    '=D0=99': 'Й',
    '=D0=9A': 'К',
    '=D0=9B': 'Л',
    '=D0=9C': 'М',
    '=D0=9D': 'Н',
    '=D0=9E': 'О',
    '=D0=9F': 'П',
    '=D0=A0': 'Р',
    '=D0=A1': 'С',
    '=D0=A2': 'Т',
    '=D0=A3': 'У',
    '=D0=A4': 'Ф',
    '=D0=A5': 'Х',
    '=D0=A6': 'Ц',
    '=D0=A7': 'Ч',
    '=D0=A8': 'Ш',
    '=D0=A9': 'Щ',
    '=D0=AA': 'Ъ',
    '=D0=AB': 'Ы',
    '=D0=AC': 'Ь',
    '=D0=AD': 'Э',
    '=D0=AE': 'Ю',
    '=D0=AF': 'Я',

    '=20': ' ',
    '=27': '`',
    '=2E': '.',
    '=2F': '/',
    '=2D': '-',
    '=5F': '_',

    '=30': '0',
    '=31': '1',
    '=32': '2',
    '=33': '3',
    '=34': '4',
    '=35': '5',
    '=36': '6',
    '=37': '7',
    '=38': '8',
    '=39': '9',

}

with open(PATH_TO_FILE, 'r') as file:
    body = file.read()

body = body.replace('=\n=', '=')

# for index in range(len(body)):
#     if body[index] == '=' and body[index + 1] == '\n' and body[index + 2] == '=':
#         pass

for key in ALPHABET.keys():
    body = body.replace(key, ALPHABET[key])

body = body.replace('=\n', '')

with open(PATH_TO_FILE + '.txt', 'w', encoding='utf-8') as file:
    file.write(body)

body = body.replace('END:VCARD\nBEGIN:VCARD', '')
body = body.replace('VERSION:2.1\n', '')
body = body.replace(';CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE', '')
re.sub('\nN:\S*\n', '\n', body)  # r'@\w+.\w+'
# re.sub(r'@\w+.\w+', '', body)  # r'@\w+.\w+'

with open(PATH_TO_FILE + '_normal.txt', 'w', encoding='utf-8') as file:
    file.write(body)

# часть по факту пришлось убирать sublime-ом, потому что re я не осилил
# \nN:\S*\n - часть так, а часть ручками
