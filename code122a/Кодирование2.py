




print("Какие система кодирования?\n"
      
      "Кодирование звука - 1\n"
      "Кодирование инофрмации - 2\n"
      "Введите цифру:")
r = int(input(""))
if r == 2:
    print("Какие данные известны?\n"
          "Напоминание:\n"
          "a - число страниц в тексте\n"
          "b - число строк на странице\n"
          "с - число символов в строке\n"
          "k - число символов в тексте\n"
          "I - информационный объём\n"
          "i - информационный вес символа\n"
          "N - мощность алфавита\n"
          "Впишите данные которые необходимо найти в вашей задаче, например: N\n"
          "Введите то что нужно найти:")

    z = str(input(""))
    if z=='N' or z== 'n':
        q2 = "Какие данные известны?"
        w = str(input('Даные:'))
        s1= "i"
        s2="I k"
        if w==s1:
            print('Введите данные:')
            i = int(input("i ="))
            N=pow(2,i)
            print (N)
        else:
            s2 = "I k"
            s3 = "k I"
            if w==('I k') or w==('k I') or w==('K I') or w==('I K'):
                print('Введите данные:')
                I = int(input("I ="))
                k = int(input("k ="))
                i = I//k
                N=pow(2,i)
                print(N)
            else:
                print('Введите данные:')
                I = int(input("I ="))
                i = int(input("i ="))
                a = int(input("a ="))
                b = int(input("b ="))
                c = int(input("c ="))
                k = a*b*c
                i=I//k
                N= pow(2,i)
                print(N)
    else:
        if z=='I':
            w = str(input('Даные:'))
            if w=='i k' or w=='k i' or w=='K i' or w=='k i':
                i = int(input("i ="))
                k = int(input("k ="))
                I=k*i
                print(I)
            if w=='N k' or w=='n k'or w== 'N K' or w=='K n':
                k = int(input("k ="))
                N = int(input("N ="))
                import math
                i = (math.log2(N))
                I = k * i
                print(I)

            else:
                i = int(input("i ="))
                a = int(input("a ="))
                b = int(input("b ="))
                c = int(input("c ="))
                k = a * b * c
                I= k*i
                print(I)
        else:
            if z=='k':
                w = str(input('Даные:'))
                s3=list('a''b''c')
                if w!= s3:
                    a = int(input("a ="))
                    b = int(input("b ="))
                    c = int(input("c ="))
                    k = a * b * c
                    print(k)
                else:
                    i = int(input("i ="))
                    I = int(input("I ="))
                    k=I//i
                    print(k)
            else:
                if z=='i':
                    e = str(input('Даные:'))
                    s4 = list('I' 'a' 'b' 'c' )
                    if e=='I k' or e=='k I' or e=='K I' or e=='I K':
                        I = int(input("I ="))
                        k = int(input("k ="))
                        i=I//k
                        print (i)
                    if e==s4:
                        I = int(input("I ="))
                        a = int(input("a ="))
                        b = int(input("b ="))
                        c = int(input("c ="))
                        k=a*b*c
                        i = I//k
                        print(i)
                    else:
                        import math
                        N = int(input("N = "))
                        print(math.log2(N))
                else:
                    print('ошибка')
if r==1:
    print("Какие данные нужно найти?\n"
          "Напоминание:\n"
          "H - частота дсикридитации (Секунда делить на шаг дискредитации)\n"
          "T - шаг дискредитации(изменение амплитуды сигналы через одинаковые промежутки вермени)\n"
          "K - квантование звука\n"
          "b - битовая глубина\n"
          "I - длина цифрового кода\n"
          "t - время записи звука\n"
          
          "Введите данные, которые вам необхадимо найти, напрмер: H\n"
          "Введите данные:")
    t=str(input())


    if t=='h' or t=='H':
        print("Какие данные известны?")
        i5 = list("I t b")
        f = str(input())
        if f == "T":
            T = int(input("введите T ="  ))
            H = 1/T
            print(H)
        if f==("I t b") or f==("I b t") or f==("t I b") or f==("t b I") or f==("b I t") or f==("b I t") :
            I = int(input("Введите I ="))
            t = int(input("Введите t = "))
            b = int(input("Введиет b ="))
            H = I/(t*b)
            print(H)
        else:
            I = int(input("Введите I ="))
            t = int(input("Введите t = "))
            K = int(input("Введиет K ="))
            import math

            b = (math.log2(K))
            H = I/(t*b)
            print(H)
    if t == 'T' :
        print("Какие данные известны?")
        f = str(input())
        if f=="H" or f=="h":
            H = int(input("Введите H ="))
            T =1/H
            print(T)
        else:
            print("Вам изветсна b?\n"
                  "Да - 1\n"
                  "Нет - 2\n")
            u = int(input())
            if u==1:
                t = int(input("Введите t = "))
                b = int(input("Введиет b ="))
                I = int(input("Введите I ="))
                H = I / (t * b)
                T = 1 / H
                print(T)
            else:
                I = int(input("Введите I ="))
                t = int(input("Введите t = "))
                K = int(input("Введиет K ="))
                import math

                b = (math.log2(K))
                H = I / (t * b)
                T = 1 / H
                print(T)
    if t == 'I'or t=="i":
        print("Какие данные известны?")
        f = str(input())
        if f==("H t b") or f==("H b t") or f==("t H b") or f==("t b H") or f==("b H t") or f==("b H t") :
            H = int(input("Введите H ="))
            t = int(input("Введите t = "))
            b = int(input("Введиет b ="))
            I = b*t*H
            print(I)
        else:
            H = int(input("Введите H ="))
            t = int(input("Введите t = "))
            K = int(input("Введиет K ="))
            import math

            b = (math.log2(K))
            I = b * t * H
            print(I)
    if t == 't':
        print("Какие данные известны?")
        f = str(input())
        if f==("H I b") or f==("H b I") or f==("I H b") or f==("I b H") or f==("b H I") or f==("b H I") :
            H = int(input("Введите H ="))
            I = int(input("Введите I ="))
            b = int(input("Введиет b ="))
            t = I/(H*b)
            print(t)
        if f == ("T I b") or f == ("T b I") or f == ("I T b") or f == ("I b T") or f == ("b T I") or f == ("b T I"):
            I = int(input("Введите I ="))
            b = int(input("Введиет b ="))
            T = int(input("введите T ="))
            H = 1 / T
            t = I / (H * b)
            print(t)
        if f == ("T I k") or f == ("T k I") or f == ("I T k") or f == ("I k T") or f == ("k T I") or f == ("k T I"):
            I = int(input("Введите I ="))
            T = int(input("введите T ="))
            K = int(input("Введиет K ="))
            import math

            b = (math.log2(K))
            H = 1 / T
            t = I / (H * b)
            print(t)
        if f == ("H I k") or f == ("H k I") or f == ("H I k") or f == ("H k I") or f == ("k H I") or f == ("k H I"):
            H = int(input("Введите H ="))
            I = int(input("Введите I ="))
            K = int(input("Введиет K ="))
            import math

            b = (math.log2(K))
            t = I / (H * b)
            print(t)
    if t == 'k':
        print("Какие данные известны?")
        f = str(input())
        if f=='b':
            b = int(input("Введиет b ="))
            K =pow(2,b)
            print(K)
        if f == ("H I t") or f == ("H t I") or f == ("H I t") or f == ("H I t") or f == ("t H I") or f == ("t H I"):
            H = int(input("Введите H ="))
            I = int(input("Введите I ="))
            t = int(input("Введите t = "))
            b = I/(H*t)
            K = pow(2, b)
            print(K)
        else:
            T = int(input("введите T ="))
            I = int(input("Введите I ="))
            t = int(input("Введите t = "))
            H = 1 / T
            b = I / (H * t)
            K = pow(2, b)
            print(K)
    if t == 'b':
        print("Какие данные известны?")
        f = str(input())
        if f == ("H I t") or f == ("H t I") or f == ("H I t") or f == ("H I t") or f == ("t H I") or f == ("t H I"):
            H = int(input("Введите H ="))
            I = int(input("Введите I ="))
            t = int(input("Введите t = "))
            b = I / (H * t)
            print(b)



        if f == ("T I t") or f == ("T t I") or f == ("I T t") or f == ("I t T") or f == ("t T I") or f == ("t T I"):
            I = int(input("Введите I ="))
            T = int(input("введите T ="))

            t = int(input("Введите t = "))
            H = 1 / T
            b = I / (H * t)

            print(b)
        if f=="k" or f=="K":
            K = int(input("Введиет K ="))
            import math

            b = (math.log2(K))

            print(b)


input()
