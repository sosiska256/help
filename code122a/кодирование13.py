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


    standart_values = {
        'i': 8
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
i  (Инф. объём символа) [ <b>, B, KB, MB, GB, TB ] = 8
K  (Количество символов в тексте)
Kt (Текст) (Только для дано)
--------------------------
Дано -> ''').split(';'))) # var=val unit(optional) | splitted with ;
    given = {var.strip(): (convert(standart_values[var.strip()], basic_units[var.strip()]['system'], (val.split()[1] if len(val.split()) > 1 else None)) if val.split()[0] == '*' and var.strip() in standart_values.keys() else (convert(val.split()[0], basic_units[var]['system'], val.split()[1] if len(val.split()) > 1 else basic_units[var]['base']) if var in basic_units.keys() else val.split()[0])) for var, val in g}
    
    t_f = list(map(lambda x: x.split('-'), input('Найти -> ').split())) # var-unit(optional) | splitted with space
    to_find = {var[0].strip(): (list(map(lambda x: x.strip(), var[1].split(','))) if len(var) > 1 else [basic_units[var[0]]['base']] if var[0] in basic_units else None) for var in t_f}
    
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
                    print(Fore.YELLOW + f'WARN! Unable to find {Style.BRIGHT + f"{var}" + Style.NORMAL}.')
            
            case 'K':
                if 'I' in given.keys() and 'i' in given.keys() and given['i'] != 0:
                    result['K'] = [given['I'] / given['i']]
                elif 'I' in given.keys() and 'N' in given.keys() and given['N'] > 1:
                    result['K'] = [given['I'] / ceil(log2(given['N']))]
                elif 'K' in given.keys():
                    result['K'] = [given['K']]
                else:
                    print(Fore.YELLOW + f'WARN! Unable to find {Style.BRIGHT + f"{var}" + Style.NORMAL}.')
            
            case 'i':
                if 'I' in given.keys() and 'k' in given.keys() and given['K'] != 0:
                    result['i'] = [str(convert(given['I'] / given['K'], basic_units['i']['system'], basic_units['i']['base'], to=u)) + f' {u}' for u in units]
                elif 'N' in given.keys() and given['N'] > 0:
                    result['i'] = [str(convert(ceil(log2(given['N'])), basic_units['i']['system'], basic_units['i']['base'], to=u)) + f' {u}' for u in units]
                elif 'i' in given.keys():
                    result['i'] = [str(convert(given['i'], basic_units['i']['system'], basic_units['i']['base'], to=u)) + f' {u}' for u in units]
                else:
                    print(Fore.YELLOW + f'WARN! Unable to find {Style.BRIGHT + f"{var}" + Style.NORMAL}.')
            
            case 'N':
                if 'i' in given.keys():
                    result['N'] = [2**given['i']]
                elif 'I' in given.keys() and 'K' in given.keys() and given['K'] > 1:
                    result['N'] = [2**(given['I'] / given['K'])]
                elif 'K' in given.keys():
                    result['N'] = [given['N']]
                else:
                    print(Fore.YELLOW + f'WARN! Unable to find {Style.BRIGHT + f"{var}" + Style.NORMAL}.')
            
            case _:
                print(Fore.YELLOW + f'WARN! Unknown variable to find {Style.BRIGHT + f"{var}" + Style.NORMAL}.\nIf uoy meant something else, please restsrt the programm.')
    
    # print(result)
    for var, res in result.items():
        print(f'{var} = {"; ".join(map(str, res))}')


def sound():
    g = list(map(lambda x: x.strip().split('='), input('''\n\n\nМожно использовать:
I  (Инф. объём Файла) [ <b>, B, KB, MB, GB, TB ]
D  (Частота дискретизации) [ Hz, <KHz>, MHz ]
t  (Время звучания) [ <s>, m, h, d ]
i (Глубина кодирования) [ <b>, B, KB, MB, GB, TB ]
--------------------------
Дано -> ''').split(';'))) # var=val unit(optional) | splitted with ;
    given = {var.strip(): (standart_values[var.strip()] if val == '*' and var.strip() in standart_values.keys() else (convert(val.split()[0], basic_units[var]['system'], val.split()[1] if len(val.split()) > 1 else basic_units[var]['base']) if var in basic_units.keys() else val.split()[0])) for var, val in g}
    
    t_f = list(map(lambda x: x.split('-'), input('Найти -> ').split())) # var-unit(optional) | splitted with space
    to_find = {var[0].strip(): (list(map(lambda x: x.strip(), var[1].split(','))) if len(var) > 1 else [basic_units[var[0]]['base']] if var[0] in basic_units else None) for var in t_f}


    
def f13():
    if input('''Перед использованием советую прочитать инструкцию
0. -- Инструкция
не 0. Далее
-> ''') == '0':
        input('''\n\n\nnot ready yet ;) I'm sorry
\n>>>''') # * = basic

    match input('''\n\n\nВыберите тип задачи
--------------------------
1. Кодирование информации
2. Кодирование звука (indev)
3. Кодирование изображений (indev)
--------------------------
-> ''')[0]:
        case '1':
            information()
        case '2':
            sound()

if __name__ == '__main__':
    f13()
    input()
