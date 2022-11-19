import math
        
q = input('Напиште номер типа задачи: \n1. Выбор неизвестного\n2. Выбор известного\n')

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
                    K = int(input('K = '))
                    i = int(input('i = '))
                    print(f'I = {K * i}')

                case 'K':
                    I = int(input('I = '))
                    i = int(input('i = '))
                    print(f'K = {I / i}')
                case 'i':
                    N = int(input('N = '))
                    if N == '':
                        I = int(input('I = '))
                        K = int(input('K = '))
                        print(f'i = {I / K}')
                    else:
                        print(f'i = {math.log2(N)}')
                case 'N':
                    i = int(input('i = '))
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
                    I = int(input('I = '))
                    M = int(input('M = '))
                    t = int(input('t = '))
                    k = int(input('k = '))
                    print(f'V = {I * M * t * k}')

                case 'I':
                    V = int(input('V = '))
                    M = int(input('M = '))
                    t = int(input('t = '))
                    k = int(input('k = '))
                    print(f'I = {V / (M * t * k)}')

                case 'M':
                    V = int(input('V = '))
                    I = int(input('I = '))
                    t = int(input('t = '))
                    k = int(input('k = '))
                    print(f'M = {V / (I * t * k)}')

                case 't':
                    V = int(input('V = '))
                    M = int(input('M = '))
                    I = int(input('I = '))
                    k = int(input('k = '))
                    print(f't = {V / (I * M * k)}')

                case 'k':
                    V = int(input('V = '))
                    M = int(input('M = '))
                    I = int(input('I = '))
                    t = int(input('t = '))
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
                    i = int(input('i = '))
                    X = int(input('X = '))
                    Y = int(input('Y = '))
                    print(f'I = {i * X * Y}')

                case 'i':
                    I = int(input('I = '))
                    X = int(input('X = '))
                    Y = int(input('Y = '))
                    print(f'i = {I / (X * Y)}')

                case 'X':
                    I = int(input('I = '))
                    i = int(input('i = '))
                    Y = int(input('Y = '))
                    print(f'i = {I / (i * Y)}')

                case 'Y':
                    I = int(input('I = '))
                    i = int(input('i = '))
                    X = int(input('X = '))
                    print(f'i = {I / (i * X)}')
    
        A = input('Тип задачи: \n1. Текстовая информация \n2. Звуковая информация \n3. Графическая информация\n')
        match A:
            case '1':
                text()
            case '2':
                sound()
            case '3':
                picture()
            
if q == '2':    
    A = input('Тип задачи: \n1. Текстовая информация \n2. Звуковая информация \n3. Графическая информация\n')
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
                    i = math.log2(int(N))
                    print(f'i = {i}')
                elif i == '' and K != '' and I != '':
                    i = int(I) / int(K)
                    print(f'i = {i}')
                    
                if I == '':
                    print(f'I = {int(K) * int(i)}')
                        
                if K == '':
                    print(f'K = {int(I) / int(i)}')
                    
                if N == '':
                    print(f'N = {2**int(i)}')
                        
                        
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
                    print(f'V = {int(I) * int(M) * int(t) * int(k)}')

                if I == '':
                    print(f'I = {int(V) / (int(M) * int(t) * int(k))}')

                if M == '':
                    print(f'M = {int(V) / (int(I) * int(t) * int(k))}')

                if t == '':
                    print(f't = {int(V) / (int(I) * int(M) * int(k))}')

                if k == '':
                    print(f'M = {int(V) / (int(I) * int(M) * int(t))}')


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
                    print(f'I = {int(i) * int(X) * int(Y)}')

                if i == '':
                    print(f'i = {int(I) / (int(X) * int(Y))}')

                if X == '':
                    print(f'X = {int(I) / (int(i) * int(Y))}')

                if Y == '':
                    print(f'Y = {int(I) / (int(i) * int(X))}')
