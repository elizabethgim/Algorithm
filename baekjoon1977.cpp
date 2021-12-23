//baekjoon1977

#include <iostream>
#include <cmath>
#include <list>

int main()
{
	int min_range, max_range;
	std::cin>>min_range>>max_range;
	list<int> perfect;

	for(int i=min_range;i<max_range+1;i++)
	{
		unsigned int num;
		num = (unsigned int)(sqrt(i));
		if(num == i)
		{
			perfect.push_back(i);
		}
	}
	
	std::cout<<perfect<<std::endl;
}