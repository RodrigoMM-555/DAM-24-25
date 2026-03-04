#include <stdio.h>

int calculoDoble(int numero){
	int doble = numero*2;
    return doble;
}

int main(){
    int edad = 47;
    int resultado = calculoDoble(edad);
    printf("El doble de tu edad es: %d \n", resultado);
    return 0;
}