from math import log2, ceil
from colorama import init
init(autoreset=True)
from colorama import Fore, Back, Style


def information():
    systems = {
        'b-TB': {'b': 1, 'B': 8, 'KB': 8*1024, 'MB': 8*(1024**2), 'GB': 8*(1024**3), 'TB': 8*(1024**4)}
    }
    

    basic_units = {
        'I': {'system': 'b-TB', 'base': 'b'},
        'i': {'system': 'b-TB', 'base': 'b'}
    }


    def convert(val: str | int | float, system: str, from_: str, to: str | None = None) -> float | int:
        try:
            if to is None:
                return eval(str(val)) * systems[system][from_]
            else:
                return eval(str(val)) * systems[system][from_] / systems[system][to]
        except IndexError as e:
            raise
        except ValueError as e:
            raise
    
    
    
    g = list(map(lambda x: x.strip().split('='), input('''\n\n\nМожно использовать:
N  (Мощность алфавита)
I  (Инф. объём текста) [ <b>, B, KB, MB, GB, TB ]
i  (Инф. объём символа) [ <b>, B, KB, MB, GB, TB ]
K  (Количество символов в тексте)
Kt (Текст) (Только для дано)
--------------------------
Дано -> ''').replace(',', '.').split(';'))) # var=val unit(optional) | splitted with ;
    given = {var.strip(): (convert(val.split()[0], basic_units[var]['system'], val.split()[1] if len(val.split()) > 1 else basic_units[var]['base']) if var in basic_units.keys() else val.split()[0]) for var, val in g}
    
    t_f = list(map(lambda x: x.split('-'), input('Найти -> ').split())) # var-unit(optional) | splitted with space
    to_find = {var[0].strip(): (list(map(lambda x: x.strip(), var[1].split(','))) if len(var) > 1 else list(systems[basic_units[var[0]]['system']].keys()) if var[0] in basic_units else None) for var in t_f}
    
    # print(given, to_find)
    
    if 'Kt' in given.keys():
        given['K'] = len(given['Kt'])
    if 'K' in given.keys():
        given['K'] = int(given['K'])
    if 'N' in given.keys():
        given['N'] = int(given['N'])
    
    # print(given, to_find)
    result = {}
    
    for var, units in to_find.items():
        match var:
            case 'I':
                if 'K' in given.keys() and 'i' in given.keys():
                    result['I'] = [str(convert(given['K'] * given['i'], basic_units['I']['system'], basic_units['I']['base'], to=u)) + f' {u}' for u in units]
                elif 'K' in given.keys() and 'N' in given.keys() and given['N'] > 0:
                    result['I'] = [str(convert(given['K'] * ceil(log2(given['N'])), basic_units['I']['system'], basic_units['I']['base'], to=u)) + f' {u}' for u in units]
                elif 'I' in given.keys():
                    result['I'] = [str(convert(given['I'], basic_units['I']['system'], basic_units['I']['base'], to=u)) + f' {u}' for u in units]
                else:
                    print(Fore.YELLOW + f'WARN! Unable to find {Style.BRIGHT + f"{var}" + Style.NORMAL}. Not enough data.')
            
            case 'K':
                if 'I' in given.keys() and 'i' in given.keys() and given['i'] != 0:
                    result['K'] = [given['I'] / given['i']]
                elif 'I' in given.keys() and 'N' in given.keys() and given['N'] > 1:
                    result['K'] = [given['I'] / ceil(log2(given['N']))]
                elif 'K' in given.keys():
                    result['K'] = [given['K']]
                else:
                    print(Fore.YELLOW + f'WARN! Unable to find {Style.BRIGHT + f"{var}" + Style.NORMAL}. Not enough data.')
            
            case 'i':
                if 'I' in given.keys() and 'K' in given.keys() and given['K'] != 0:
                    result['i'] = [str(convert(given['I'] / given['K'], basic_units['i']['system'], basic_units['i']['base'], to=u)) + f' {u}' for u in units]
                elif 'N' in given.keys() and given['N'] > 0:
                    result['i'] = [str(convert(ceil(log2(given['N'])), basic_units['i']['system'], basic_units['i']['base'], to=u)) + f' {u}' for u in units]
                elif 'i' in given.keys():
                    result['i'] = [str(convert(given['i'], basic_units['i']['system'], basic_units['i']['base'], to=u)) + f' {u}' for u in units]
                else:
                    print(Fore.YELLOW + f'WARN! Unable to find {Style.BRIGHT + f"{var}" + Style.NORMAL}. Not enough data.')
            
            case 'N':
                if 'i' in given.keys():
                    result['N'] = [2**given['i']]
                elif 'I' in given.keys() and 'K' in given.keys() and given['K'] > 1:
                    result['N'] = [2**(given['I'] / given['K'])]
                elif 'K' in given.keys():
                    result['N'] = [given['N']]
                else:
                    print(Fore.YELLOW + f'WARN! Unable to find {Style.BRIGHT + f"{var}" + Style.NORMAL}. Not enough data.')
            
            case _:
                print(Fore.YELLOW + f'WARN! Unknown variable to find {Style.BRIGHT + f"{var}" + Style.NORMAL}.\nIf you meant something else, please restsrt the programm.')
    
    # print(result)
    for var, res in result.items():
        print(f'{var} = {"; ".join(map(str, res))}')


def sound():
    systems = {
        'b-TB': {'b': 1, 'B': 8, 'KB': 8*1024, 'MB': 8*(1024**2), 'GB': 8*(1024**3), 'TB': 8*(1024**4)},
        's-d': {'s': 1, 'm': 60, 'h': 60*60, 'd': 60*60*24},
        'Hz-MHz': {'Hz': 1, 'KHz': 1000, 'MHz': 1000**2}
    }
    

    basic_units = {
        'I': {'system': 'b-TB', 'base': 'b'},
        'i': {'system': 'b-TB', 'base': 'b'},
        't': {'system': 's-d', 'base': 's'},
        'D': {'system': 'Hz-MHz', 'base': 'KHz'}
    }


    def convert(val: str | int | float, system: str, from_: str, to: str | None = None) -> float | int:
        try:
            if to is None:
                return eval(str(val)) * systems[system][from_]
            else:
                return eval(str(val)) * systems[system][from_] / systems[system][to]
        except IndexError as e:
            raise
        except ValueError as e:
            raise
    
    
    
    g = list(map(lambda x: x.strip().split('='), input('''\n\n\nМожно использовать:
I (Инф. объём Файла) [ <b>, B, KB, MB, GB, TB ]
D (Частота дискретизации) [ Hz, <KHz>, MHz ]
t (Время звучания) [ <s>, m, h, d ]
i (Глубина кодирования) [ <b>, B, KB, MB, GB, TB ]
k (Количество каналов) = 1
--------------------------
Дано -> ''').replace(',', '.').split(';'))) # var=val unit(optional) | splitted with ;
    given = {var.strip(): (convert(val.split()[0], basic_units[var]['system'], val.split()[1] if len(val.split()) > 1 else basic_units[var]['base']) if var in basic_units.keys() else val.split()[0]) for var, val in g}
    
    t_f = list(map(lambda x: x.split('-'), input('Найти -> ').split())) # var-unit(optional) | splitted with space
    to_find = {var[0].strip(): (list(map(lambda x: x.strip(), var[1].split(','))) if len(var) > 1 else list(systems[basic_units[var[0]]['system']].keys()) if var[0] in basic_units else None) for var in t_f}
    # I = k * D * t * i / 8
    if 'k' in given.keys():
        given['k'] = int(given['k'])
    if 'k' not in given.keys() and 'k' not in to_find.keys():
        given['k'] = 1
    
    result = {}
    
    for var, units in to_find.items():
        match var:
            case 'I':
                if 'I' in given.keys():
                    result['I'] = [str(convert(given['I'], basic_units['I']['system'], basic_units['I']['base'], to=u)) + f' {u}' for u in units]
                elif 'k' in given.keys() and 'D' in given.keys() and 't' in given.keys() and 'i' in given.keys():
                    result['I'] = [str(convert(given['k'] * given['D'] * given['t'] * given['i'], basic_units['I']['system'], basic_units['I']['base'], to=u)) + f' {u}' for u in units]
                else:
                    print(Fore.YELLOW + f'WARN! Unable to find {Style.BRIGHT + f"{var}" + Style.NORMAL}. Not enough data.')
            case 'k':
                if 'k' in given.keys():
                    result['k'] = [given['k']]
                elif 'I' in given.keys() and 'D' in given.keys() and 't' in given.keys() and 'i' in given.keys():
                    result['k'] = [given['I'] / (given['D'] * given['t'] * given['i'])]
                else:
                    print(Fore.YELLOW + f'WARN! Unable to find {Style.BRIGHT + f"{var}" + Style.NORMAL}. Not enough data.')
            case 'D':
                if 'D' in given.keys():
                    result['D'] = [str(convert(given['D'], basic_units['D']['system'], basic_units['D']['base'], to=u)) + f' {u}' for u in units]
                elif 'k' in given.keys() and 'I' in given.keys() and 't' in given.keys() and 'i' in given.keys():
                    result['D'] = [str(convert(given['I'] / (given['k'] * given['t'] * given['i']), basic_units['D']['system'], basic_units['D']['base'], to=u)) + f' {u}' for u in units]
                else:
                    print(Fore.YELLOW + f'WARN! Unable to find {Style.BRIGHT + f"{var}" + Style.NORMAL}. Not enough data.')
            case 't':
                if 't' in given.keys():
                    result['t'] = [str(convert(given['t'], basic_units['t']['system'], basic_units['t']['base'], to=u)) + f' {u}' for u in units]
                elif 'k' in given.keys() and 'I' in given.keys() and 'D' in given.keys() and 'i' in given.keys():
                    result['t'] = [str(convert(given['I'] / (given['k'] * given['D'] * given['i']), basic_units['t']['system'], basic_units['t']['base'], to=u)) + f' {u}' for u in units]
                else:
                    print(Fore.YELLOW + f'WARN! Unable to find {Style.BRIGHT + f"{var}" + Style.NORMAL}. Not enough data.')
            case 'i':
                if 'i' in given.keys():
                    result['i'] = [str(convert(given['i'], basic_units['i']['system'], basic_units['i']['base'], to=u)) + f' {u}' for u in units]
                elif 'k' in given.keys() and 'I' in given.keys() and 'D' in given.keys() and 't' in given.keys():
                    result['i'] = [str(convert(given['I'] / (given['k'] * given['D'] * given['t']), basic_units['i']['system'], basic_units['i']['base'], to=u)) + f' {u}' for u in units]
                else:
                    print(Fore.YELLOW + f'WARN! Unable to find {Style.BRIGHT + f"{var}" + Style.NORMAL}. Not enough data.')
            
            case _:
                print(Fore.YELLOW + f'WARN! Unknown variable to find {Style.BRIGHT + f"{var}" + Style.NORMAL}.\nIf you meant something else, please restsrt the programm.')
    
    # print(result)
    for var, res in result.items():
        print(f'{var} = {"; ".join(map(str, res))}')


def picture():
    systems = {
        'b-TB': {'b': 1, 'B': 8, 'KB': 8*1024, 'MB': 8*(1024**2), 'GB': 8*(1024**3), 'TB': 8*(1024**4)}
    }
    

    basic_units = {
        'V': {'system': 'b-TB', 'base': 'b'},
        'i': {'system': 'b-TB', 'base': 'b'},
    }


    def convert(val: str | int | float, system: str, from_: str, to: str | None = None) -> float | int:
        try:
            if to is None:
                return eval(str(val)) * systems[system][from_]
            else:
                return eval(str(val)) * systems[system][from_] / systems[system][to]
        except IndexError as e:
            raise
        except ValueError as e:
            raise
    
    
    
    g = list(map(lambda x: x.strip().split('='), input('''\n\n\nМожно использовать:
V (Объём видеопамяти) [ <b>, B, KB, MB, GB, TB ]
N (Количество цветов)
r (Количество пикселей)
i (Глубина цвета) [ <b>, B, KB, MB, GB, TB ]
x (Количество пикселей по горизонтали)
y (Количество пикселей по вертикали)
--------------------------
Дано -> ''').replace(',', '.').split(';'))) # var=val unit(optional) | splitted with ;
    given = {var.strip(): (convert(val.split()[0], basic_units[var]['system'], val.split()[1] if len(val.split()) > 1 else basic_units[var]['base']) if var in basic_units.keys() else val.split()[0]) for var, val in g}
    
    t_f = list(map(lambda x: x.split('-'), input('Найти -> ').split())) # var-unit(optional) | splitted with space
    to_find = {var[0].strip(): (list(map(lambda x: x.strip(), var[1].split(','))) if len(var) > 1 else list(systems[basic_units[var[0]]['system']].keys()) if var[0] in basic_units else None) for var in t_f}
    # V = i * r
    
    if 'N' in given.keys():
        given['i'] = ceil(log2(int(given['N'])))
    elif 'i' in given.keys():
        given['N'] = 2**given['i']
    if 'x' in given.keys() and 'y' in given.keys():
        given['r'] = given['x'] * given['y']
    elif 'r' in given.keys() and 'y' in given.keys():
        given['x'] = given['r'] / given['y']
    elif 'r' in given.keys() and 'x' in given.keys():
        given['y'] = given['r'] / given['x']
    
    result = {}

    for var, units in to_find.items():
        match var:
            case 'V':
                if 'V' in given.keys():
                    result['V'] = [str(convert(given['V'], basic_units['V']['system'], basic_units['V']['base'], to=u)) + f' {u}' for u in units]
                elif 'i' in given.keys() and 'r' in given.keys():
                    result['V'] = [str(convert(given['i'] * given['r'], basic_units['V']['system'], basic_units['V']['base'], to=u)) + f' {u}' for u in units]
                else:
                    print(Fore.YELLOW + f'WARN! Unable to find {Style.BRIGHT + f"{var}" + Style.NORMAL}. Not enough data.')
                
            case 'i':
                if 'i' in given.keys():
                    result['i'] = [str(convert(given['i'], basic_units['i']['system'], basic_units['i']['base'], to=u)) + f' {u}' for u in units]
                elif 'V' in given.keys() and 'r' in given.keys():
                    result['i'] = [str(convert(given['V'] / given['r'], basic_units['i']['system'], basic_units['i']['base'], to=u)) + f' {u}' for u in units]
                else:
                    print(Fore.YELLOW + f'WARN! Unable to find {Style.BRIGHT + f"{var}" + Style.NORMAL}. Not enough data.')
                
            case 'r':
                if 'r' in given.keys():
                    result['r'] = [given['r']]
                elif 'V' in given.keys() and 'i' in given.keys():
                    result['r'] = [given['V'] / given['i']]
                else:
                    print(Fore.YELLOW + f'WARN! Unable to find {Style.BRIGHT + f"{var}" + Style.NORMAL}. Not enough data.')
                
            case 'x':
                if 'x' in given.keys():
                    result['x'] = [given['x']]
                else:
                    print(Fore.YELLOW + f'WARN! Unable to find {Style.BRIGHT + f"{var}" + Style.NORMAL}. Not enough data.')
            
            case 'y':
                if 'y' in given.keys():
                    result['y'] = [given['y']]
                else:
                    print(Fore.YELLOW + f'WARN! Unable to find {Style.BRIGHT + f"{var}" + Style.NORMAL}. Not enough data.')
            
            case 'N':
                if 'N' in given.keys():
                    result['N'] = [given['N']]
                else:
                    print(Fore.YELLOW + f'WARN! Unable to find {Style.BRIGHT + f"{var}" + Style.NORMAL}. Not enough data.')
            
            case _:
                print(Fore.YELLOW + f'WARN! Unknown variable to find {Style.BRIGHT + f"{var}" + Style.NORMAL}.\nIf you meant something else, please restsrt the programm.')
                    
    # print(result)
    for var, res in result.items():
        print(f'{var} = {"; ".join(map(str, res))}')
    
    
def f13():
    if input('''Перед использованием советую прочитать инструкцию
0. -- Инструкция
не 0. Далее
-> ''') == '0':
        input('''\n\n\nПосле выбора типа задачи вам будет предложен список возможных значений.
Пример строчки такого списка: "i (Глубина кодирования) (только для дано) [ <b>, B, KB, MB, GB, TB ] = 1"

Первым идёт Обозначение перемнной, потом в скобках указано её название на человеческом языке.
Затем в ещё одних скобках может быть указано, что данную переменную можно использовать только в дано.

Потом у переменных, которые могут иметь различные еденицы измерения, перечислены эти самые единицы измерения,
и в <> находится то значение, которое будет использовано по умалчанию, если не указать иного.

Ну и у некоторых переменных, которые частенико не указывают в дано, потому что подразумевают некоторое базовое значение,
может быть указано значение, которое будет дано данной перемнной, если её не указать ни в Дано, ни в Найти

При вводе "Дано" надо учитывать 5 правил:
    1.  Данные значения перечисляются через ;
    2.  Каждое значение должно быть записано как Обозначение перемнной и её значение разделённые знаком =
    3.  К значению переменной можно дописать единицу измерения в которой она дана, записав через пробел.
    4.  Не ставьте лишних пробелов, не все они првильно обрабатываются.
    5.  Учитывайте регистр Обозначений перемнных

Пример строчки из дано (из решения задачи кодирования информации): "Дано -> I=6 B;K=3"

При вводе "Найти" надо учитывать 4 правила:
    1.  Переменные для нахождения перечисляются через пробел
    2.0 При желании можно указать конкретные единицы измерения для вывода
    2.1 Эти еденицы приписываются к Обозначению переменной через - и перечисляются через ,
    2.2 По умолчанию вывод будет во всех доступных единицах измерения.
    3.  Не ставьте лишних пробелов, не все они првильно обрабатываются.
    4.  Учитывайте регистр Обозначений перемнных

Email для связи - night_skumbry@outlook.com

\n>>>''')

    match input('''\n\n\nВыберите тип задачи
--------------------------
1. Кодирование информации (неправильное сообщение при ошибке деления на ноль)
2. Кодирование звука (пока не знает ошибки)
3. Кодирование изображений (пока не знает ошибки)
--------------------------
Писать там -> ''')[0]:
        case '1':
            information()
        case '2':
            sound()
        case '3':
            picture()
        case 'счастье':
            print('I can\'t help you, but you still can read the instruction. ☻')
        case _:
            print('You must stry again.')

if __name__ == '__main__':
    while True:
        f13()
        input('Нажмите Enter ')

