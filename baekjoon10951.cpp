#include <iostream>
using namespace std;

int main()
{
    cin.tie(NULL); ios::sync_with_stdio(false);
    int num1, num2;

    while(!(cin >>num1>>num2).eof())
    {
        cout<<num1+num2<<"\n";
    }
}