#include <stdio.h>

int main(){
	int escierto = 4 == 4 && 3 == 3 && 2 == 2;
	printf("%i",escierto);
    printf("\n");
	int esfalso = 4 == 4 && 3 == 3 && 2 == 1;
	printf("%i",esfalso);
    printf("\n");

    escierto = 4 == 4 || 3 == 3 || 2 == 1;
    printf("%i",escierto);
    printf("\n");
    escierto = 4 == 4 || 3 == 1 || 2 == 1;
    printf("%i",escierto);
    printf("\n");
    esfalso = 4 == 1 || 3 == 1 || 2 == 1;
    printf("%i",esfalso);
  return 1;
}