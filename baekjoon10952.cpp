#include <iostream>
using namespace std;

int main()
{
    cin.tie(NULL); ios::sync_with_stdio(false);
    
    int num1, num2;

    while((num1 + num2 != 0))
    {   
        cin>>num1>>num2;
        if(num1 != 0 && num2 != 0) {
            cout<<num1+num2<<"\n";
        }
        
    }
}