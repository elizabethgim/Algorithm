//baekjoon11021

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
        int result=0;
        result = data1+data2;
        std::cout<<"Case #"<<i+1<<": "<<result<<"\n";
    }

}