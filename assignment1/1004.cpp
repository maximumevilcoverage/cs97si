#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
int main(){
    double sum=0; double temp;
    while(cin >> temp){
        sum += temp;
    }
    cout <<"$" << sum / 12.0;
}
