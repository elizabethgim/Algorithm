#include <iostream>
#include <vector>

using namespace std;

int fibonacci(int num){
    if(num == 1) return 1;
    else if (num == 2) return 1;
    else return fibonacci(num-1)+fibonacci(num-2);
}

int main(){
    int num;
    cin >> num;

    cout << fibonacci(num) << endl;
    return 0;
}