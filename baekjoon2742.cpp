#include <iostream>

int main()
{
    int num;
    std::cin.tie(NULL);
    std::ios::sync_with_stdio(false);
    std::cin>>num;
    for(int i=num;i>0;i--)
    {
        std::cout<<i<<"\n";
    }
}