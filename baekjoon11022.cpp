//baekjoon11022

#include <iostream>

int main()
{
    std::cin.tie(NULL);
    std::ios::sync_with_stdio(false);

    int numTestCase;
    int data1, data2;

    std::cin>>numTestCase;

    for(int i =0;i<numTestCase;i++)
    {
        std::cin >> data1 >> data2;
        std::cout<<"Case #"<<i+1<<": "<<data1<<" + "<<data2<<" = "<<data1+data2<<"\n";
    }

}