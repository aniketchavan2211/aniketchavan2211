#include <stdio.h>

int main() {
    int num1, num2;
    int sum, diff, mul, div;
    char op;

    printf("Calculator\n\n");
    printf("Please Enter first value: \n");
    scanf(" %d", &num1);
    printf("\nPlease enter operation: [+, -, *, /]\n");
    scanf(" %s", &op);
    printf("\nPlease enter second value: \n");
    scanf(" %d", &num2);
    // printf("%d,%s,%d", num1, op, num2);
 
    if (op == '+') {
        sum = num1+num2;
        printf("\nAddition of %d + %d is: %d: ", num1, num2, sum);
    }
    else if (op == '-') {
        diff = num1-num2;
        printf("Difference of %d - %d is: %d: ", num1, num2, diff);
    }
    else if (op == '*') {
        mul = num1*num2;
        printf("Multiplication of %d * %d is: %d: ", num1, num2, mul);
    }
    else if (op == '/') {
        div = num1/num2;
        printf("Divde %d / %d is: %d: ", num1, num2, div);
    }
    else {
        printf("Please enter a valid operator!");
    }
    getchar();
}