#include <stdio.h>
#include <math.h>

int main()
{
    int numTestCases, x1, y1, r1, x2, y2, r2, answer = 0;
    scanf("%d", &numTestCases);
    for(int i=0;i<numTestCases;i++){
        scanf("%d %d %d %d %d %d", &x1, &y1, &r1, &x2, &y2, &r2);
        int sub, sum;
        sum = r1+r2;
        if(r1>r2){
            sub = r1-r2;
        }else{
            sub = r2- r1;
        }

        double d;

        d = sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
        if(sum == d || sub == d){
            answer = 1;
        }else if(sub > d && sum < d){
            answer = 0;
        }else{
            answer = 2;
        }
        printf("%d\n", answer);
    }
}
