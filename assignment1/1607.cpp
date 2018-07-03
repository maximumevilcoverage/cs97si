#include <iostream>
#include <algorithm>
#include <string>
#include <cmath>
#include <iomanip>
typedef long double ld;
typedef long long ll;
using namespace std;
int main()
{
    int cards;
    cout.setf(ios::fixed,ios::floatfield);
    cout.precision(3);
    cout << "Cards  Overhang\n";
    while(cin>>cards)
    {
        double sum=0;
        for (int i=0; i < cards; i++){
            sum += 1.0/(2*(i+1));
        }
        cout << setw(5) << cards << "     " << sum << '\n';
    }
    return 0;
}
