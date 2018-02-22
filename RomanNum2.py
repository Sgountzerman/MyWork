def akeraios_se_rom(arith):
    latin=""
    while arith!=0:
        if (arith>=500000):
            if (arith>=900000):
                latin += "-C-M"
                arith-=900000
            else:
                latin += "-D"
                arith -=500000
        elif (arith>=100000):
            if arith>= 400000:
                latin +="-C-D"
                arith -=400000
            else:
                latin +="-C"
                arith -=100000
        elif(arith >= 50000):
            if(arith>= 90000):
                latin +="-X-C"
                arith -=90000
            else:
                latin +="-L"
                arith -=50000
        elif(arith >= 10000):
            if(arith>=40000):
                latin +="-X-L"
                arith -=40000
            else:
                latin+="-X"
                arith-=10000
        elif(arith>=5000):
            if(arith>=9000):
                latin+="M-X"
                arith-=9000
            else:
                latin+="-V"
                arith-=5000
        elif(arith>=1000):
            if(arith>=4000):
                latin +="M-V"
                arith -=4000
            else:
                latin +="M"
                arith -=1000
        elif(arith>=500):
            if arith>=900:
                latin+="CM"
                arith-=900
            else:
                latin+="D"
                arith-=500
        elif arith>=100:
            if arith >=400:
                latin+="CD"
                arith-=400
            else:
                latin +="C"
                arith -=100
        elif arith >=50:
            if arith >=90:
                latin +="XC"
                arith -=90
            else:
                latin +="L"
                arith -=50
        elif arith >=10:
            if arith >=40:
                latin +="XL"
                arith -=40
            else:
                latin +="X"
                arith -= 10
        elif arith >=5:
            if arith >=9:
                latin +="IX"
                arith -=9
            else:
                latin +="V"
                arith -=5
        elif arith >=1:
            if arith >=4:
                latin +="IV"
                arith -=4
            else:
                latin +="I"
                arith -=1

    return latin

arithmos=int(input("Give me a number:"))
print (akeraios_se_rom(arithmos))

