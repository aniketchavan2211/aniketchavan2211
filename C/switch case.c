// Illustrating the switch statement

#include <stdio.h>
// #include <conio.h>

int main() {
    char Grade = 'A';
    switch(Grade) {
        case 'A': printf("\nExcellence\n");
            break;
        case 'B': printf("\nGood\n");
            break;
        case 'C': printf("\nFine\n");
            break;
        case 'D': printf("\nOK\n");
            break;
        case 'E': printf("\nYou must do better than this\n");
            break;
        default: printf("\nWhat is your grade anyway");
            break;
    }
    // getch();
    return 0;
}