#include <stdio.h>

void main()
{
    int num1, num2, num3;
    scanf("%d %d %d", &num1, &num2, &num3);
    int sum = num1 * num2 * num3;
    char numbers;
    // numbers = (char)sum;
    printf("%d\n%d\n%d\n", num1, num2, num3);
    printf("num : %d\n", sum);
    // printf("%c\n", numbers);
}