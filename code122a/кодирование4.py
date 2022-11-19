import math 
def otvet(a):
    print("В каких еденицах нужен ответ? (бит/байт/килобайт/мегабайт/гигабайт/терабайт)")
    G=input()
    if G=="бит":
        a=str(str(a)+" бит")
    elif G=="байт":
        a=str(str(a/2**3)+" байт")
    elif G=="килобайт":
        a=str(str(a/2**13)+" килобайт")
    elif G=="мегабайт":
        a=str(str(a/2**23)+" мегабайт")
    elif G=="гигабайт":
        a=str(str(a/2**33)+" гигабайт")
    elif G=="терабайт":
        a=str(str(a/2**43)+" терабайт")
    print(a)
def perevod(a,b):
    if b== "байт":
        a=a*2**3
    elif b== "килобайт":
        a=a*2**13
    elif b== "мегабайт":
        a=a*2**23
    elif b== "гигабайт":
        a=a*2**33
    return a 
def it(N):
    T = int(math.log2(2*N-1))
    return T
def pamyat():
    N ="1 - Мощность алфавита(N), "
    K ="2 - колво символов в тексте(K), "
    I ="3 - инф объём текста(I), "
    i ="0 - инф  символа(i), "
    print("что нужно найти? (",i,N,K,I,")")
    G=input()
    if G=="0":
        N=input("N-?\n")
        K=int(input("K-?\n"))
        I,V=float(input("I-?\n")),input("бит/байт/килобайт/мегабайт/гигабайт?\n")
        if N=="":
            otvet(K*perevod(I,V))
        else: 
            otvet(it(int(N)))
    if G=="1":
        i,v=float(input("i-?\n"))
        print(2**perevod(i,v))
    if G=="3":
        K=int(input("K-?\n"))
        N=input("N-?\n")
        i,V=input("i-?\n"),input("бит/байт/килобайт/мегабайт/гигабайт?\n")
        if i=="":
             I=it(int(N))*K
        else:
            I=perevod(float(i),V)*K
        otvet(I)
    if G=="2":
        I,V1=float(input("I-?\n")),input("бит/байт/килобайт/мегабайт/гигабайт?\n")
        i,V2=input("i-?\n"),input("бит/байт/килобайт/мегабайт/гигабайт?\n")
        N=input("N-?\n")
        if i=="":
            K=perevod(I,V1)/it(int(N))
        else:
            K=perevod(I,V1)/perevod(float(i),V2)
        print(K)
def zvuk():
    N ="0 - количество уровней сигнала(N), "
    D ="1 - частота дискретизации(D), "
    V ="2 - объём звуковоо файла(V), "
    i ="3 - глубина звука(i), "
    T ="4 - длительность звукового файла(T)"
    print("Что нужно найти? (",N,D,V,i,T,")")
    G=input()
    if G=="0":
        i,b=float(input("i-?\n")),input("бит/байт/килобайт/мегабайт/гигабайт?\n")
        print(2**perevod(i,b))
    if G=="1":
        N=input("N-?\n")
        i,b1=input("i-?\n"),input("бит/байт/килобайт/мегабайт/гигабайт?\n")
        T=float(input("T-?\n"))
        V,b2=float(input("V-?\n")),input("бит/байт/килобайт/мегабайт/гигабайт?\n")
        if i =="":
            print(perevod(V,b2)/(it(int(N))*T))
        else:
            print(perevod(V,b2)/(perevod(i,b1)*T))
    if G=="2":
        D=float(input("D-?\n"))
        i,b1=input("i-?\n"),input("бит/байт/килобайт/мегабайт/гигабайт?\n")
        N=input("N-?\n")
        T=float(input("T-?\n"))
        if i =="":
            print(D*(it(int(N))*T))
        else:
            print(D*(perevod(i,b1)*T))
    if G=="3":
        N=input("N-?\n")
        T=float(input("T-?\n"))
        V,b2=float(input("V-?\n")),input("бит/байт/килобайт/мегабайт/гигабайт?\n")
        D=float(input("D-?\n"))
        if N=="":
            otvet(perevod(V,b2)/(D*T))
        else:
            otvet(it(int(N)))
    if G=="4":
        N=input("N-?\n")
        i,b1=input("i-?\n"),input("бит/байт/килобайт/мегабайт/гигабайт?\n")
        V,b2=float(input("V-?\n")),input("бит/байт/килобайт/мегабайт/гигабайт?\n")
        D=float(input("D-?\n"))
        if i =="":
            otvet(perevod(V,b2)/(perevod(i,b1)*D))
        else:
            otvet(perevod(V,b2)/(it(int(N))*D))
def isobr():
    N ="0 - количество цветов в политре(N), "
    H ="1 - высота изображения(H), "
    W ="2 - ширина изображения(W), "
    i ="3 - глубина текста(i), "
    I ="4 - инф объём изображения(I), "
    print("Что нужно найти? (",N,i,H,W,")")
    G=input()
    if G=="0":
        i,b1=input("i-?\n"),input("бит/байт/килобайт/мегабайт/гигабайт?\n")
        print(2**perevod(i,b1))
    if G=="1":
        i,b1=input("i-?\n"),input("бит/байт/килобайт/мегабайт/гигабайт?\n")
        N=input("N-?\n")
        W=int(input("W-?\n"))
        I,b2=float(input("I-?\n")),input("бит/байт/килобайт/мегабайт/гигабайт?\n")
        if i=="":
            print(perevod(I,b2)/(it(int(N))*W))
        else:
            print(perevod(I,b2)/(perevod(i,b1)*W))
    if G=="2":
        i,b1=input("i-?\n"),input("бит/байт/килобайт/мегабайт/гигабайт?\n")
        N=input("N-?\n")
        H=int(input("H-?\n"))
        I,b2=float(input("I-?\n")),input("бит/байт/килобайт/мегабайт/гигабайт?\n")
        if i=="":
            print(perevod(I,b2)/(it(int(N))*H))
        else:
            print(perevod(I,b2)/(perevod(i,b1)*H))
    if G=="3":
        N=input("N-?\n")
        W=int(input("W-?\n"))
        I,b2=float(input("I-?\n")),input("бит/байт/килобайт/мегабайт/гигабайт?\n")
        N=input("N-?\n")
        if N=="":
            otvet(perevod(I,b2)/(H*W))
        else:
            otvet(it(int(N)))
    if G=="4":
        N=input("N-?\n")
        H=int(input("H-?\n"))
        W=int(input("W-?\n"))
        i,b1=input("i-?\n"),input("бит/байт/килобайт/мегабайт/гигабайт?\n")
        if i =="":
            otvet(W*(it(int(N))*H))
        else:
            otvet(W*(perevod(i,b1)*H))
print("Какой тип задачи нужно решить? (звук, текст, изобр)")
A=input()
if A=="звук":
    zvuk()
if A=="текст":
    pamyat()
if A=="изобр":
    isobr()
