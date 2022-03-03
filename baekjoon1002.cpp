#include <iostream>
#include <cmath>
using namespace std;

int main(){
    int numTestCases;
    int x1, y1, r1, x2, y2, r2;

    for(int i=0; i<numTestCases; i++){
        cin >> x1 >> y2>> r1>> x2>> y2>> r2;
        cout << x1 << y2 << x2 <<y2 <<r2;

        int x = pow((x2-x1), 2);
        int y = pow((y2-y1), 2);
        int d = pow((x+y), 0.5);

        if(r1 < r2){
            int temp;
            temp = r1;
            r1 = r2;
            r2 = temp;
        }

        if(d == r1+ r2){
            cout << 1;
        }else if(d > r1+ r2 && d > r1 - r2){
            cout << 0;
        }else{
            cout << 2;
        }
        cout<<"/n";
    }
}