
tonas=[]
events=[]

def notas(tonas):
    w=0
    while w==0:
        o=0
        print("\n¿Que quieres hacer?")
        o=int(input("1. Nueva nota\n2. Mostrar nota \n3. Borrar nota \n4. Atras\n5. Debug\n"))
        
        if o==1:#cre una lista con titutlo y nota
            t=input("Titulo: ")
            n=input()
            nota=[t,n]
            tonas.append(nota)#mete esa lista en otra lista 
        
        elif o==2 and len(tonas)!=0:
            b=1
            n=0
            print("\n¿Que nota quieres?")
            for a in tonas:
                print(b,".",a[0])#muestra los titulos de las notas
                b+=1
            x=int(input())#que numero de nota quieres
            for a in tonas:
                n+=1
                if x==n: #encuentra la nota que quieres y la muestra
                    print("Titulo:",a[0])
                    print(a[1])
            
        elif o==3 and len(tonas)!=0:
            b=1
            n=0
            print("\n¿Que nota quieres borrar?")
            for a in tonas:
                print(b,".",a[0])#muestra los titulos de las notas
                b+=1
            x=int(input())
            for a in tonas:
                n+=1
                if x==n:
                    del tonas[x-1]# borra la nota seleccionada
                    print("Nota",a[0],"borrada")
        
        elif o==4:
            w=1

        elif o==5:
            print(events)
            print(len(events))
        
        elif len(events)==0:
            print("No hay notas")
        
        else:
            print("Opcion invalida")


def calendario():n4
    w=0
    while w==0:
        o=0
        print("\n¿Que quieres hacer?")
        o=int(input("1. Nuevo evento\n2. Mostrar eventos \n3. Borrar evento \n4. Atras\n5. Debug\n"))
        
        if o==1:
            dia=int(input("Dia: "))
            mes=int(input("Mes: "))
            e=input("Evento:")
            ev=[dia,mes,e]
            events.append(ev)
            
        elif o==4:
            w=1

        elif o==5:
            print(tonas)
            print(len(tonas))
        
        elif len(tonas)==0:
            print("No hay eventos")
        
        else:
            print("Opcion invalida")
        

def main():
    w=0
    o=0
    while w==0:
        print("¿Que quieres hacer?")
        o=int(input("1. Notas \n2. Calendario\n3. \n4. Cerrar\n"))
        
        if o==1:
            notas(tonas)
            main()
        
        elif o==4:
            w=1
        
        else:
            print("Opcion invalida\n")
    
main()



















