//baekjoon2438

#include <iostream>

int main()
{
    std::cin.tie(NULL);
    std::ios::sync_with_stdio(false);

    int numStar;
    std::cin>>numStar;

    for(int i = 0;i<numStar;i++)
    {
        char star;
        star='*';

        for (int j=0;j<i+1;j++)
        {
            std::cout<<star;
        }
        std::cout<<"\n";
    }

}