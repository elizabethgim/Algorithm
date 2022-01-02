#include <iostream>

int main()
{
    std::cin.tie(NULL);
    std::ios::sync_with_stdio(false);

    int numTestCases, num, max, min;
    std::cin>>numTestCases;
    std::cin >>num;
    min = num;
    max = num;

    for(int i=0; i<numTestCases-1;i++)
    {
        std::cin>>num;
        if(num < min){
            min = num;
        }
        if(num > max)
        {
            max = num;
        }
    }

    std::cout<<min<<" "<<max<<"\n";
}