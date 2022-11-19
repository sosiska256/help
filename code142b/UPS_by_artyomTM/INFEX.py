import CALC
types_of_act_for_InfEx=["0", "1", "2", "3", "4", "5", "6"]
def for_img():
#   TODO чтение перем. M и ans (см. GLOBALS)
    try:
        CFlg=0
        UP=input("I want to find:\n\t0- I want to go out\n\t1-i\n\t2-k\n\t3-I\n\t4-calc\n>>>")
        if not (UP in types_of_act_for_InfEx):
            raise
        elif UP=="1":
            I=eval(input("I in bits >>>"))
            k=eval(input("k >>>"))
            ans=I/k
            print(ans)
        elif UP=="2":
            I=eval(input("I in bits >>>"))
            i=eval(input("i in bits >>>"))
            ans=I/i
            print(ans)
        elif UP=="3":
            i=eval(input("i in bits >>>"))
            k=eval(input("k >>>"))
            ans=i*k
            print(ans)
        elif UP=="4":
            CFlg=1
            CALC.calc()
#       TODO запись перем. M и ans (см. GLOBALS)        
        if CFlg==0:
            clc=input("calc - ? (1-yes; 0-no)>>>")
            if clc=="1":
                CALC.calc()
    except:
        print("ERROR!!!\nEND OF WORK!!!")
def for_text():
#   TODO чтение перем. M и ans (см. GLOBALS)
    try:
        CFlg=0
        UP=input("I want to find:\n\t0- I want to go out\n\t1-i\n\t2-k\n\t3-I\n\t4-calc\n>>>")
        if not (UP in types_of_act_for_InfEx):
            raise
        elif UP=="1":
            I=eval(input("I in bits >>>"))
            k=eval(input("k >>>"))
            ans=I/k
            print(ans)
        elif UP=="2":
            I=eval(input("I in bits >>>"))
            i=eval(input("i in bits >>>"))
            ans=I/i
            print(ans)
        elif UP=="3":
            i=eval(input("i in bits >>>"))
            k=eval(input("k >>>"))
            ans=i*k
            print(ans)
        elif UP=="4":
            CFlg=1
            CALC.calc()
#       TODO запись перем. M и ans (см. GLOBALS)        
        if CFlg==0:
            clc=input("calc - ? (1-yes; 0-no)>>>")
            if clc=="1":
                CALC.calc()
    except:
        print("ERROR!!!\nEND OF WORK!!!")
def for_aud():
#   TODO чтение перем. M и ans (см. GLOBALS)
    try:
        CFlg=0
        UP=input("I want to find:\n\t0- I want to go out\n\t1-i\n\t2-k\n\t3-t\n\t4-f\n\t5-I\n\t6-calc\n>>>")
        if not (UP in types_of_act_for_InfEx):
            raise
        elif UP=="1":
            I=eval(input("I in bits >>>"))
            k=eval(input("k >>>"))
            t=eval(input("t >>>"))
            f=eval(input("f >>>"))
            ans=I/(k*t*f)
            print(ans)
        elif UP=="2":
            I=eval(input("I in bits >>>"))
            i=eval(input("i in bits >>>"))
            t=eval(input("t >>>"))
            f=eval(input("f >>>"))
            ans=I/(i*t*f)
            print(ans)
        elif UP=="3":
            I=eval(input("I in bits >>>"))
            i=eval(input("i in bits >>>"))
            k=eval(input("k >>>"))
            f=eval(input("f >>>"))
            ans=I/(i*k*f)
            print(ans)
        elif UP=="4":
            I=eval(input("I in bits >>>"))
            i=eval(input("i in bits >>>"))
            k=eval(input("k >>>"))
            t=eval(input("t >>>"))
            ans=I/(i*k*t)
            print(ans)
        elif UP=="5":
            t=eval(input("t >>>"))
            i=eval(input("i in bits >>>"))
            k=eval(input("k >>>"))
            f=eval(input("f >>>"))
            ans=i*k*f*t
            print(ans)
        elif UP=="6":
            CFlg=1
            CALC.calc()
#       TODO запись перем. M и ans (см. GLOBALS)        
        if CFlg==0:
            clc=input("calc - ? (1-yes; 0-no)>>>")
            if clc=="1":
                CALC.calc()
    except:
        print("ERROR!!!\nEND OF WORK!!!")
def InfEx():
    try:
        while True:
            tp = input("I want to:\n\t0-exit\n\t1-image\n\t2-text\n\t3-audio\n\t4-calc\n>>>")
            if not (tp in types_of_act_for_InfEx):
                raise
            if tp=="0":
                break
            elif tp=="1":
                for_img()
            elif tp=="2":
                for_text()
            elif tp=="3":
                for_aud()
            elif tp=="4":
                CALC.calc()
    except:
        print("ERROR!!!\nEND OF WORK!!!")
