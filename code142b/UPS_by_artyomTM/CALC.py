from math import *
import GLOBALS
def calc():
#   TODO чтение перем. M и ans (см. GLOBALS)
    while True:
        try:
            inp=input("CALC>>>")
            if inp=="exit":
                break
            else:
                ans=eval(inp)
                print(ans)
        except:
            print("ERROR")
#   TODO запись перем. M и ans (см. GLOBALS)
