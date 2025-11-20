

edad_mago=input("Introduce la edad del mago: ")
cate=""
escudo=15
daño=0

############################################

try:
    edad_mago=int(edad_mago)
except:
    edad_mago=100

####################################

if edad_mago<30:
    cate="Aprendiz"
elif 30<=edad_mago<=99:
    cate="Hechicero"
else:
    cate="Archimago"

########################################

def poderBase(edad_mago):
    if edad_mago<30:
        return 5
    elif 30<=edad_mago<=99:
        return 8
    else:
        return 10
        
###################################

print("El mago es de rango",cate,", tiene",edad_mago,"años y su nivel de poder es de",poderBase(edad_mago))

##################################

t=1
while escudo!=0:
    for turno in range(1,3):
        print("Turno",t,", el escudo tiene",escudo,"de energia")
        if turno==1:
            print("El",cate,"lanza ¡Bola de fuego!")
            daño=poderBase(edad_mago)//2
            escudo-=daño
        elif turno==2:
            print("El",cate,"lanza ¡Rayooo!")
            daño=poderBase(edad_mago)//3
            escudo-=daño
        if escudo<0:
            escudo=0
        print("El escudo a recivido",daño,"puntos de daño.")
        t+=1
        if escudo==0:
            break
print("El escudo se ha roto")

########################################



    

