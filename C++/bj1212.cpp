#include <iostream>
#include <string>
using namespace std;

int main(){
    string eight;
    cin >> eight;

    string two[8] = {"000", "001", "010", "011", "100", "101", "110", "111"};
    int temp;

    for(int i=0;i<eight.length();i++){
        temp = eight[i] - '0';
        if (i==0){
            cout << stoi(two[temp]);
        } else{
            cout << two[temp];
        }
    }
    
    return 0;
}