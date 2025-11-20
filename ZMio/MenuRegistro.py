
# Online Python - IDE, Editor, Compiler, Interpreter


def registro():
    o=0
    lista=[0,0,0]
    print(lista)
    
    lista[0]=input("Dame tu nombre: ")
    lista[1]=input("\nDame tus apellidos: ")
    
    while o==0:
        d=input("\nDame tu DNI: ")
        if len(d)!=9:
            print("\nTe falta o sobra algun digito")
        else:
            o=1
            lista[2]=d
    return(lista)


def menu():
    o=0
    print("¿Que quieres hacer?")
    o=input("1. Registrarme\n2. \n3. \n4. Cerrar\n")
    return(o)


def main():
    w=0
    while w=0:
        h=menu()
        print(h)
        if h==1:
            registro()
        if h==2:
            
        if h==3:
            
        if h==4:
            w=1
        


main()