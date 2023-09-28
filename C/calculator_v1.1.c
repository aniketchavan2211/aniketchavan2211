#include <stdio.h>

int main() {
    // Declare and Initialize variable
    int num1, num2;
    double sum, difference, product, divsior;
    char operator;

    // Input and Output
    printf("\n# Calculator #\n\n");
    printf("Please enter first number: \n");
    scanf(" %d: \n", &num1);

    printf("Please enter second number: \n");
    scanf(" %d: \n", &num2);

    printf("Select Operator: [+, -, *, /] ");
    scanf("%c: \n", &operator);

    // Calculation
    sum = num1+num2;
    difference = num1-num2;
    product = num1*num2;
    divsior = num1/num2;

    // switch case
    switch (operator) {
    case '+':
        printf("Addition of %d + %d is: %d", num1, num2, sum);
        break;
    case '-':
        printf("Difference of %d - %d is: %d", num1, num2, difference);
        break;
    case '*': 
        printf("Multiplication of %d * %d is: %d", num1, num2, product);
        break;
    case '/':
        printf("Division of %d / %d is: %d", num1, num2, divsior);
        break;
    default: 
        printf("E: Some went wrong!");
    }

    // return function
    return 0;
}