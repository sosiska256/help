def f12():

    import math
        
    q = input('Напиште номер типа задачи: \n1. Выбор неизвестного\n2. Выбор известного')

    if q == '1':
        def text():
            print('''
    I = K * i
    N = 2^i
    I - Количество информации в сообщении (в битах)
    K - Количество символов в сообщении
    i - Информационный вес символа (в битах)
    N - Мощность алфавита''')

            ans = input('Напишите что необходимо найти I, K, i, N: ')

            match ans:
                case 'I':
                    K = input('K = ')
                    i = input('i = ')
                    print(f'I = {K * i}')

                case 'K':
                    I = input('I = ')
                    i = input('i = ')
                    print(f'K = {I / i}')
                case 'i':
                    N = input('N = ')
                    if N == '':
                        I = input('I = ')
                        K = input('K = ')
                        print(f'i = {I / K}')
                    else:
                        print(f'i = {math.log2(N)}')
                case 'N':
                    i = input('i = ')
                    print(f'N = {2**i}')

        def sound():
            print('''
    V = I * M * t * k
    V - Объём звукового файла (в битах)
    I - Глубина кодирования звука (в битах)
    M - Частота дискретизации звука
    t - Длительность звучания файла (в секундах)
    k - Количество каналов звучания''')
            ans = input('Напишите что необходимо найти V, I, M, t, k: ')

            match ans:
                case 'V':
                    I = input('I = ')
                    M = input('M = ')
                    t = input('t = ')
                    k = input('k = ')
                    print(f'V = {I * M * t * k}')

                case 'I':
                    V = input('V = ')
                    M = input('M = ')
                    t = input('t = ')
                    k = input('k = ')
                    print(f'I = {V / (M * t * k)}')

                case 'M':
                    V = input('V = ')
                    I = input('I = ')
                    t = input('t = ')
                    k = input('k = ')
                    print(f'M = {V / (I * t * k)}')

                case 't':
                    V = input('V = ')
                    M = input('M = ')
                    I = input('I = ')
                    k = input('k = ')
                    print(f't = {V / (I * M * k)}')

                case 'k':
                    V = input('V = ')
                    M = input('M = ')
                    I = input('I = ')
                    t = input('t = ')
                    print(f'k = {V / (I * M * t)}')

        def picture():
            print('''
    I = i * X * Y
    I - Информационный объём (в битах)
    i - Глубина цвета (в битах)
    X - Ширина изображения (в пикселях)
    Y - Высота изображения (в пикселях)''')
            ans = input('Напишите что необходимо найти I, i, X, Y: ')

            match ans:
                case 'I':
                    i = input('i = ')
                    X = input('X = ')
                    Y = input('Y = ')
                    print(f'I = {i * X * Y}')

                case 'i':
                    I = input('I = ')
                    X = input('X = ')
                    Y = input('Y = ')
                    print(f'i = {I / (X * Y)}')

                case 'X':
                    I = input('I = ')
                    i = input('i = ')
                    Y = input('Y = ')
                    print(f'i = {I / (i * Y)}')

                case 'Y':
                    I = input('I = ')
                    i = input('i = ')
                    X = input('X = ')
                    print(f'i = {I / (i * X)}')

            A = input('Тип задачи: \n1. Текстовая информация \n2. Звуковая информация \n3. Графическая информация')
    
        match A:
            case '1':
                text()
            case '2':
                sound()
            case '3':
                picture()
            
    if q == '2':    
        A = input('Тип задачи: \n1. Текстовая информация \n2. Звуковая информация \n3. Графическая информация')
        print('Если значение отсутствует, нажмите Enter')
        match A:
            case '1':   
                print('''
    I = K * i
    N = 2^i
    I - Количество информации в сообщении (в битах)
    K - Количество символов в сообщении
    i - Информационный вес символа (в битах)
    N - Мощность алфавита''')
                I = input('I = ')
                K = input('K = ')
                i = input('i = ')
                N = input('N = ')
                    
                if i == '' and N != '':
                    i = math.log2(N)
                    print(f'i = {i}')
                elif i == '' and K != '' and I != '':
                    i = I / K
                    print(f'i = {i}')
                else:
                    print('Ошибка')
                    
                if I == '':
                    print(f'I = {K * i}')
                else:
                    print('Ошибка')
                        
                if K == '':
                    print(f'K = {I / i}')
                else:
                    print('Ошибка')
                    
                if N == '':
                    print(f'N = {2^i}')
                        
                        
            case '2':
                print('''
    V = I * M * t * k
    V - Объём звукового файла (в битах)
    I - Глубина кодирования звука (в битах)
    M - Частота дискретизации звука
    t - Длительность звучания файла (в секундах)
    k - Количество каналов звучания''')
                V = input('V = ')
                I = input('I = ')
                M = input('M = ')
                t = input('t = ')
                k = input('k = ')

                if V == '':
                    print(f'V = {I * M * t * k}')

                if I == '':
                    print(f'I = {V / (M * t * k)}')

                if M == '':
                    print(f'M = {V / (I * t * k)}')

                if t == '':
                    print(f't = {V / (I * M * k)}')

                if k == '':
                    print(f'M = {V / (I * M * t)}')


            case '3':
                print('''
I = i * X * Y
I - Информационный объём (в битах)
i - Глубина цвета (в битах)
X - Ширина изображения (в пикселях)
Y - Высота изображения (в пикселях)''')
                I = input('I = ')
                i = input('i = ')
                X = input('X = ')
                Y = input('Y = ')

                if I == '':
                    print(f'I = {i * X * Y}')

                if i == '':
                    print(f'i = {I / (X * Y)}')

                if X == '':
                    print(f'X = {I / (i * Y)}')

                if Y == '':
                    print(f'Y = {I / (i * X)}')
