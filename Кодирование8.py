import math
def aboba():
    print("1.Сколько байт и бит займёт слово")
    print("2.Сколько символов в слове")
    print("3.Сколько байт в одном символе")
    n=int(input("Зачем оно тебе надо (если выбрали не то введите 0):"))
    if n==1:
        b=int(input("Сколько символов (если выбрали не то введите 0)="))
        c=int(input("Сколько байт в одном символе=")) 
        if b<=0 or c<=0:
            print("Неверный ввод")
            aboba()
        else :
            a=b*c
            print("Размер="+str(a) + "Байт")
    elif n==2:
        a=int(input("Сколько байт (если выбрали не то введите 0)="))
        c=int(input("Сколько байт в одном символе="))
        if a<=0 or c<=0:
            print("Неверный ввод!")
            aboba()
        else :
            b=a/c
            print (str(b) + "символов")
    elif n==3:
        a=int(input("Сколько байт (если выбрали не то введите 0)"))
        b=int(input("Сколько символов"))
        if a<=0 or b<=0:
            print("Неверный ввод")
            aboba()
        else :
            c=a/b
            print ("Байт в одном символе="+str(c) )
    else:
        print("Неверный ввод!")    
    
def amogus():
    print("1.Размер аудиофайла")
    print("2.Частота")
    print("3.Время звучания")
    print("4.Разрядность регистра")
    n=int(input("Зачем оно тебе надо (если выбрали не то введите 0):"))
    if n==1:
        D=int(input("Частота (если выбрали не то введите 0)="))
        T=int(input("Время звучания="))
        I=int(input("Разрядность регистра (бит)="))
        if D<=0 or T<=0 or I<=0:
            print("Неверный ввод")
            amogus()
        else:
            a=D*T*I/8
            print(str(a) + "Бит")
    elif n==2:
        A=int(input("Размер (если выбрали не то введите 0)="))
        T=int(input("Время звучания="))
        I=int(input("Разрядность регистра (бит)="))
        if A<=0 or T<=0 or I<=0:
            print("Неверный ввод")
            amogus()
        else:
            D=8*A/(T*I)
            print ("Частота="+str(D))
    elif n==3:
        A=int(input("Размер (если выбрали не то введите 0)="))
        D=int(input("Частота="))
        I=int(input("Разрядность регистра="))
        if A<=0 or D<=0 or I<=0:
            print("Неверный ввод")
            amogus()
        else:
            T=8*A/(D*I)
            print ("Время звучания="+str(T))
    elif n==4:
        A=int(input("Размер (если выбрали не то введите 0)="))
        T=int(input("Время звучания="))
        D=int(input("Частота="))
        if D<=0 or T<=0 or A<=0:
            print("Неверный ввод")
            amogus()
        else:
            I=8*A/(T*I)
            print ("Разрядность регистра="+str(I))
    else:
        print("Неверный ввод!")    

def abobus():
    print("1.Размер изображения")
    print("2.Глубина цвета через размер")
    print("3.Глубина цвета через количество цвето")
    print("4.Количество цветов")
    print("5.Количество пикселей")
    n=int(input("Зачем оно тебе надо (если выбрали не то введите 0):"))
    if n==1:
        I=int(input("Глубина (бит) (если выбрали не то введите 0)="))
        V=int(input("Количество пикселей="))
        if I<=0 or V<=0:
            print("Неверный ввод")
            abobus()
        else :
            a=V*I
            print(str(a) + "Бит")
    elif n==3:
        N=int(input("Количество цветов (если выбрали не то введите 0)="))
        if N<=0:
            print("Неверный ввод")
            abobus()
        else:
            I=math.log(N,2)
            print ("Глубина цвета="+str(I))
    elif n==3:
        A=int(input("Размер (байт) (если выбрали не то введите 0)="))
        V=int(input("Количество пикселей="))
        if A<=0 or V<=0:
            print("Неверный ввод")
            abobus()
        else :
            I=A*V
            print("Глубина"+str(a/8))
    elif n==4:
        I=int(input("Глубина цвета (бит) (если выбрали не то введите 0)="))
        if I<=0:
            print("Неверный ввод")
            abobus()
        else :
            N=2**I
            print ("Количество цветов="+str(N))
    elif n==5:
        A=int(input("Размер (если выбрали не то введите 0)="))
        I=int(input("Глубина="))
        if I<=0 or A<=0:
            print("Неверный ввод")
            abobus()
        else :
            V=A/I
            print ("Разрядность регистра="+str(V))
    else:
        print("Неверный ввод!")    

def menu1():
    print("1.Текстовые задачи")
    print("2.Звуковые задачи")
    print("3.Графические задачи")
    a=int(input("Шо тебе надо?"))
    if a==1:
        aboba()
    elif a==2:
        amogus()
    elif a==3:
        abobus()
    else:
        print("Неверный ввод!")
while 1 >0:
    menu1()
