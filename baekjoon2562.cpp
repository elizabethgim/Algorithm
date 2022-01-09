#include <iostream>

int main()
{
    std::cin.tie(NULL);
    std::ios::sync_with_stdio(false);

    int i, num, cnt, max;
    cnt = 0;
    max = 0;

    for(i=0;i<9;i++)
    {
        std::cin>>num;
        if(num > max){
            max = num;
            cnt = i+1;
        }
    }

    std::cout<<max<<"\n";
    std::cout<<cnt<<"\n";
}