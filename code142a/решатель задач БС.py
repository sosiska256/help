
print("Какую задачу нужно решить: a,b,c")
a = "a) кодирование информации"
b = "b) кодирование звука"
c = "c) кодирование изображения"
print(a)
print(b)
print(c)
bukva = input("Выберите вид задачи"" ")
print("вид задачи")
if bukva == "a":
    print("выбор неизвестного: I,N,i,K")
    a = "I) информационный объем"
    b = "N) мощность алфавита(кол-во символовв алфавите)"
    c = "i) вес одного символа"
    d = "K) число знаков в тексте"
    print(a)
    print(b)
    print(c)
    print(d)
    neizvestnoe = input("Выберите неизвестное"" ")
    
    if neizvestnoe == "I":
        i = int(input("Введите i "" "))
        K = int(input("Введите K"" "))
        I = K*i
        print('информационный объем', I)
    elif neizvestnoe == "N":
        print("Введите i")
        i= int(input())
        N = 2**i
        print('мощность алфавита(кол-во символовв алфавите', N)
    elif neizvestnoe == "i":
        I = int(input("Введите I"" "))
        K = int(input("Введите K"" "))
        i = I/K
        print('вес одного символа',i)
    elif neizvestnoe == "K":
        I = int(input("Введите I"" "))
        i = int(input("Введите i"" "))
        K = I/i
        print('число знаков в тексте',
              K)
elif bukva == "b":
    print("выбор неизвестного:I, H, t, b, K ")
    a = "I) объем звуковой информации"
    b = "H) частота дискретизации"
    c = "t) время записи звука"
    d = "b) разрядность квантования"
    e = "e) кол-во уровней квантования"
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    neizvestnoe = input("Выберите неизвестное"" ")
    
    if neizvestnoe == "I":
        H = int(input("Введите H"" "))
        t = int(input("Введите t"" "))
        b = int(input("Введите b"))
        I = H*t*b
        print('объем звуковой информации', I)
    elif neizvestnoe == "H":
        I = int(input("Введите I"" "))
        t = int(input("Введите t"" "))
        b = int(input("Введите b"" "))
        H = I/t*b
        print('частота дискретизации',H)
    elif neizvestnoe == "t":
        I = int(input("Введите I"" "))
        t = int(input("Введите t"" "))
        b = int(input("Введите b"" "))
        t = I/H*b
        print('время записи звука',t)
    elif neizvestnoe == "b":
        I = int(input("Введите I"" "))
        H = int(input("Введите H"" "))
        t = int(input("Введите t"" "))
        b = I/H*t
        print('разрядность квантования', b)
    elif neizvestnoe == "K":
        b = int(input("Введите b"" "))
        K = 2**b
        print('кол-во уровней квантования', K)
elif bukva == "c":
    print("выбор неизвестного:K, b ")
    a = "K) кол-во оттенков"
    b = "b) глубина цвета"
    print(a)
    print(b)
    neizvestnoe = input("Выберите неизвестное"" ")
    

    if neizvestnoe == "K":
        b = int(input("Введите b"" "))
        K = 2**b
        print('кол-во оттенков', K)
    elif neizvestnoe == "b":
        K = input(int("Введите K"" "))
        b = 1
        while 2**b != (int(K)):
            b = b + 1 
        print('глубина цвета', b)


