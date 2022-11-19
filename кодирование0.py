def f0():
    
    import math

    def menu11_resh(I,K,i,N,sel):

        otvet=0
        if sel==1:
            
            if K>0 and i>0:
                I=K*i
                form='I= K * i'
            elif K>0 and N>0:
                I=K*math.log2(N)
                form='I= K * log2(N)'
            otvet=I
            ed_izm='бит'

        if sel==2:
            if I>0 and i>0:
                K=I/i
                form='K=I/i'
            elif I>0 and N>0:
                K=I/math.log2(N)
                form='K=I/log2(N)'
            otvet=K
            ed_izm='символов'

        if sel==3:
            if I>0 and K>0:
                i=I/K
                form='i=I/K'
            elif N>0:
                i=math.log2(N)
                form='i=log2(N)'
            otvet=i
            ed_izm='бит'


        if sel==4:
            if I>0 and K>0:
                N=2**(I/K)
                form='N=2^(I/K)'
            elif i>0:
                N=2**i
                form='N=2^i'
            otvet=N
            ed_izm='символов'


        print(f'\nОтвет: {form}={otvet} {ed_izm}\nЗадача решена. Хотите решить еще одну? Для этого нажмите 1')
        if input('Ваш выбор-')=='1':
            f0()
        else:
            print('выход')
            exit()
        
    def menu21_resh(V,p,i,N,sel):
        #print(V,p,i,sel)
        otvet=0
        if sel==1:
            if p>0 and i>0:
                V=p*i
                form='V= p * i'
            elif p>0 and N>0:
                V=p*math.log2(N)
                form='V= p * log2(N)'
            otvet=V
            ed_izm='бит'

        if sel==2:
            if V>0 and i>0:
                p=V/i
                form='p= V / i'
            elif V>0 and N>0:
                p=V/math.log2(N)
                form='p= V/ log2(N)'
            otvet=p
            ed_izm='пикселей'

        if sel==3:
            if p>0 and V>0:
                i=V/p
                form='i= V / p'
            elif N>0:
                i=math.log2(N)
                form='i=log2(N)'
            otvet=i
            ed_izm='бит'
            
        print(f'\nОтвет: {form}={otvet} {ed_izm}\nЗадача решена. Хотите решить еще одну? Для этого нажмите 1')

    def menu31_resh(I,H,b,t,sel):
        otvet=0
        if sel==1:
            if H>0 and b>0 and t>0:
                I=H*b*t
                form='I=H*b*t'
            otvet=I
            ed_izm='бит'

        if sel==2:
            if I>0 and b>0 and t>0:
                H=I/b*t
                form='H=I/b*t'
            otvet=H
            ed_izm='Герц'

        if sel==3:
            if I>0 and H>0 and t>0:
                b=I/H*t
                form='b=I/H*t'
            otvet=b
            ed_izm='бит'

        if sel==4:
            if I>0 and H>0 and b>0:
                t=I/H*b
                form='t=I/H*b'
            otvet=t
            ed_izm='с'
        
        print(f'\nОтвет: {form}={otvet} {ed_izm}\nЗадача решена. Хотите решить еще одну? Для этого нажмите 1')

    def menu11(m1,m2,m3,m4,select,sel):
        sel2=0
        m5='Закончить ввод данных'
        menu=[m1,m2,m3,m4,m5]
        print(sel, menu)
        I=K=i=N=H=t=p=V=b=-1

        if sel==1 or sel==3:  crit=5
        elif sel==2: crit=4
            
        while sel2!=crit:
            print('\nВыберите, что вам известно (если вы ошибетесь с вводом данных, можно будет ввести их заново)\n')
            
            for n in range(crit):
                if n!=select-1: print (f'{n+1}. {menu[n]}')
                else: print(f'{n+1}. Пункт активирован')

            sel2=int(input('Ваш выбор-'))
            if sel==1: velich=['I=','K=','i=','N=']
            if sel==2: velich=['V=','p=','i=','N=']
            if sel==3: velich=['I=','H=','b=','t=']
            txt='Введите значение '
            
            n=0
            if sel2!=select and sel==1:
                if sel2==n+1:I=int(input(f'{txt} {velich[n]}'))
                if sel2==n+2:K=int(input(f'{txt} {velich[n+1]}'))
                if sel2==n+3:i=int(input(f'{txt} {velich[n+2]}'))
                if sel2==n+4:N=int(input(f'{txt} {velich[n+3]}'))
                if sel2==n+5:menu11_resh(I,K,i,N,select)
            
            elif sel2!=select and sel==2:
                if sel2==n+1:V=int(input(f'{txt} {velich[n]}'))
                if sel2==n+2:p=int(input(f'{txt} {velich[n+1]}'))
                if sel2==n+3:i=int(input(f'{txt} {velich[n+2]}'))
                if sel2==n+4:N=int(input(f'{txt} {velich[n+3]}'))
                if sel2==n+5:menu21_resh(V,p,i,N,select)
            
            elif sel2!=select and sel==3:
                if sel2==n+1:I=int(input(f'{txt} {velich[n]}'))
                if sel2==n+2:H=int(input(f'{txt} {velich[n+1]}'))
                if sel2==n+3:b=int(input(f'{txt} {velich[n+2]}'))
                if sel2==n+4:t=int(input(f'{txt} {velich[n+3]}'))
                if sel2==n+5:menu11_resh(I,H,b,t,select)
            elif sel2==select:
                print('Этот пункт уже активирован!')
                input('Нажмите любую клавишу')
                     
    def menu1():
        print(text)
        if sel==1:
            m1='I - информационный объем сообщения'
            m2='K - количество символов'
            m3='i - информационный вес символа'
            m4='N - мощность алфавита'
        
        if sel==2:
            m1='V - информационный объем изображения'
            m2='p (x,y) - количество пикселей'
            m3='i - информационный вес цвета (разрядность)'
            m4='N - количество цветов в палитре'
        
        if sel==3:
            m1='I - информационный объем звукового файла'
            m2='H - частота дискретизации'
            m3='b - битовая губина кодирования или разрядность квантования'
            m4='t - время звучания'

        print(f'''
    1. {m1}
    2. {m2}
    3. {m3}
    4. {m4}''',end=' ')
        
        select=int(input(f'\n{vibor}'))
        print(f'Вы выбрали {select}')
        menu11(m1,m2,m3,m4,select,sel)

    # Заготовки и настрокйки
    text='\nВыберите, что вам нужно найти'
    vibor='Ваш выбор-'
    otv='\nОтвет: {form}={otvet} {ed_izm}\nЗадача решена. Хотите решить еще одну? Для этого нажмите 1'
    m1=m2=m3=m4=''
    select1=['I','K','i','N']
    I=K=i=N=-1
    
    # Старт
    print('1. Кодирование информации\n2. Кодирование изображения\n3. Кодирование аудио')
    sel=int(input('Ваш выбор-'))
    menu1()

f0()
