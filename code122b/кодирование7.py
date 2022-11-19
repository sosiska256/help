import math

def sound():
    print("что неизвестно? (1 - объем(I),\n 2 - частота дискретизации(H)\n, 3 - время записи(t),\n 4 - разрядность квантования(b)")
    arg = int(input())
    if arg == 1:
        print("введите частоту, время, разрядность последовательно через пробел")
        H, t, b = map(int, input().split())
        res = H * t * b
        return "I = " + res
    elif arg == 2:
        print("введите объем, время, разрядность последовательно через пробел")
        I, t, b = map(int, input().split())
        res = I // (t * b)
        return "H = " + res
    elif arg == 3:
        print("введите объем, частоту, разрядность последовательно через пробел")
        I, H, b = map(int, input().split())
        res = I // (H * b)
        return "t = " + res
    elif arg == 4:
        print("введите объем, время, частоту последовательно через пробел")
        I, t, H = map(int, input().split())
        res = I // (H * t)
        return "b = " + res
    else:
        return "неверные входные данные"

def image():
    print ("что неизвестно? (1 - количество цветов(N),\n 2 - глубина избражения(i)")
    arg = int(input())
    if arg == 1:
        print("введите глубину изображения")
        i = int(input())
        res = 2 ** i
        return "N = "
    elif arg == 2:
        print("введите количество цветов")
        N = int(input())
        return math.log(N, 2)
    else:
        return "неверные входные данные"
def information():
    print("что нужно найти? (1 - информационный объем текста(I),\n 2 - мощность алфавита(N),\n 3 - количество символов(K),\n 4 - информационный вес символа(i))")
    arg = int(input())
    if arg == 1:
        print("известен ли информационный вес символа? (1 - да, 0 - нет)")
        tr = bool(input())
        if tr:
            print("введите инф вес символа, количество символов последовательно через пробел")
            i, K = map(int, input().split())
            res = i * K
            return "I = " + res
        else:
            print("введите мощность алфавита, количество символов последовательно через пробел")
            N, K = map(int, input().split())
            res = math.log2(N) * K
            return "I = " + res
    elif arg == 2:
        print("известен ли инф вес символа? 1 - да, 0 - нет")
        tr = bool(input())
        if tr:
            print("введите инф вес символа")
            i = int(input())
            res = 2 ** i
            return "N = " + res
        else:
            print("введиите инф объем текста, количество символов последовательно через пробел")
            I, K = map(int,input().split())
            res = 2 ** (I // K)
            return "N = " + res
    elif arg == 3:
        print("известен ли инф вес символа? 1 - да, 0 - нет")
        tr = bool(input())
        if tr:
            print("введите инф объем текста, инф вес символа последовательно через пробел")
            I, i = map(int, input().split())
            res = I // i
            return "K = " + res
        else:
            print("введите инф объем, мощность алфаввита поледовательно через пробел")
            I, N = map(int,input().split())
            res = I // math.log2(N)
            return "K = " + res
    elif arg == 4:
        print("через что надо найти? 1 = инф объем текста,\n 2 - мощность алфавитa")
        r = int(input())
        if r == 1:
            print("введите объем текста, количество символов последовательно через пробел")
            I, K = map(int,input().split())
            res = I // K
            return "i = " + res
        else:
            print("введите мощность алфавита")
            N = int(input())
            return "i = " + math.log2(N)
    else:
        return "неверные входные данные"

def construct(a, arg):
    #аргумент это та величина, из которой переводим, пока вся фуцкция - сертвый код
    # 1 - байт, 2 - Кб, 3 - Мб, 4 - Гб
    if arg == 1:
        return a * 2 ** 3
    elif arg == 2:
        return a * 2 ** 13
    elif arg == 3:
        return a * 2 ** 23
    elif arg == 4:
        return a * 2 ** 33
    else:
        return
   
def solve():
    print("кодирование: 1 - инфы, 2 - звука, 3 - изображения")
    n = int(input())
    if n == 1:
        res = information()
    elif n == 2:
        res = sound()
    elif n == 3:
        res = image()
    else:
        print("это не то, ты не достоин совершщеннства решения этой задачи!!!!!")
        return
    print(res)
    return

if __name__ == "__main__":
    solve()

