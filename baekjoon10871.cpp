//baekjoon 10871

#include <iostream>
using namespace std;

int main()
{
    int in_Num, Compare;
    cin >> in_Num >> Compare;
    
    for(int i=0;i<in_Num;i++)
    {
        int num;
        cin >> num;
        if (num < Compare)
        {
            cout<<num<<" ";
        }

    }
    
}