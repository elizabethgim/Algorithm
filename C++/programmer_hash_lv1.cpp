#include <iostream>
#include <string>
#include <vector>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    int completedIndex = -1;
    for(int i=0;i<participant.capacity();i++){
        for(int j=0;j<completion.capacity(); j++){
            if(participant[i] == completion[j]){
            }else{
                break;
            }
        }
    }
    return answer; 
}

int main(){
    vector <string> p = {"leo", "kiki", "eden"};
    vector <string> c = {"eden", "kiki"};
    
    for(int i=0;i<p.size();i++){
        cout << "p:" << p[i] << endl;
    }

    for(int i=0;i<c.size();i++){
        cout << "c:" << c[i] << endl;
    }
    
    cout << solution(p, c) << endl;
}