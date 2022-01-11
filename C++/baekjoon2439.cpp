//baekjoon2439

#include <iostream>

int main()
{
    std::cin.tie(NULL);
    std::ios::sync_with_stdio(false);

    int numTestCases;
    std::cin>>numTestCases;

    int i, j, k;  
    for(i=0;i<numTestCases;i++)
    {
        for(j=1;j<numTestCases-i;j++)
        {
            std::cout<<" ";
        }
        
        for(k=0;k<i+1;k++)
        {
            std::cout<<"*";
        }
        std::cout<<"\n";
    }

}