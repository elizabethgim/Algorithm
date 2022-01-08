#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    int numTestCases;
    cin>>numTestCases;
    
    for(int i =0;i<numTestCases;i++)
    {   
        int x, y = -1;
        int cnt=0;
        int num1, num2, first, sec, res = -1;
        
        cin>>x;
        y = x;

        while(res != y)
        {
            num1 = x/10;
            num2 = x%10;
            
            first = num2;
            sec = (num1+num2)%10;
            x = (first*10)+sec;
            res = x;
            cnt++;
        }

        cout<<cnt<<"\n";
    }

}