#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
int main(){
    double sum=0; double temp;
    while(cin >> temp, temp != 0.0){ //brute force, disgusting.
        sum=0; int i=1;
        while (sum < temp){
            sum += 1.0/++i;
        }
        if (i > 277) cout << "HEH";
        cout << i-1 << " card(s)\n";
    }
}
