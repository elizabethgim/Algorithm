#include <stdio.h> 

int main(void) {
    
    int a,b,c,d=-1,result,input,count=0;
    
    scanf("%d", &input);
    result = input;
    
    while(d!=result) {
        num1 = input / 10;
        num2 = input % 10; 
        c = (a+b) % 10; 
        d = (b*10) + c; 
        input = d;
        count++;
    }
    printf("%d", count);
}