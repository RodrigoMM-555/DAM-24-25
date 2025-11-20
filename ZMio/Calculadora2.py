
# Online Python - IDE, Editor, Compiler, Interpreter

i=0
n1=0
n2=0

n1=float(input(print("Dame el primer numero ")))
n2=float(input(print("Dame el segundo numero ")))


def menu(o):
    print("\n¿Que operacion quieres hacer?")

    o=int(input(print("1.Suma\n2.Resta\n3.Multiplicacion\n4.Division")))
    return(o)


def calculo(o,n1,n2):    
    if o==1:
        print(n1,"+",n2,"=",(n1+n2))
    if o==2:
        print(n1,"-",n2,"=",(n1-n2))
    if o==3:
        print(n1,"x",n2,"=",(n1*n2))
    if o==4:
        print(n1,"/",n2,"=",(n1/n2))


def principal():
    o=0
    o=menu(o)
    if o<5 and o>0:
        calculo(o,n1,n2)
    else:
        print("\nSeleccion invalida")
        principal()
        
principal()


