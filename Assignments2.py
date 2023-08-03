import math
alamat=input("Enter (sin,cos,tan,cot,!,radical,+,-,*,/)")




if alamat=="sin" or alamat=="cos" or alamat=="tan" or alamat=="cot":
    a=int(input("Enter degree:"))

    if alamat=="sin":
        print(math.sin(math.degrees(a)))
    elif alamat=="cos":
        print(math.cos(math.degrees(a)))
    elif alamat=="tan":
        print(math.tan(math.degrees(a)))
    elif alamat=="cot":
        print(1/(math.tan(math.degrees(a))))


elif alamat=="!":
    adad1=int(input("Enter adad3:"))
    if adad1==0 or adad1==1:
        print("0! is 1")
    else:
        print(math.factorial(adad1))

elif alamat=="radical":
    adad2=int(input("Enter adad2:"))
    print(math.sqrt(adad2))


elif alamat=="-" or alamat=="+" or alamat=="*" or alamat=="/" :
    adad3=int(input("Enter  adad3:"))
    adad4=int(input("Enter  adad4:"))
    if alamat=="+":
        print(adad3+adad4)
    elif  alamat=="-":
        print(adad3-adad4)
    elif alamat=="*":
        print(adad3*adad4)
    elif alamat=="/":
        if adad4==0:
            print("adad4 nabaiad 0 bashad")
        else :
            print(adad3/adad4)
    

