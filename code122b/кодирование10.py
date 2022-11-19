question = "Что нужно найти? "
print(question)
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
input()
