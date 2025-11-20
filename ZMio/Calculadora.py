
# Online Python - IDE, Editor, Compiler, Interpreter

o=0
n1=0
n2=0

n1=float(input(print("Dame el primer numero ")))
n2=float(input(print("Dame el segundo numero ")))

print("\n¿Que operacion quieres hacer?")

if o!=1 or 2 or 3 or 4:
    o=int(input(print("1.Suma\n2.Resta\n3.Multiplicacion\n4.Division")))

if o==1:
    print(n1,"+",n2,"=",(n1+n2))
if o==2:
    print(n1,"-",n2,"=",(n1-n2))
if o==3:
    print(n1,"x",n2,"=",(n1*n2))
if o==4:
    print(n1,"/",n2,"=",(n1/n2))
    
