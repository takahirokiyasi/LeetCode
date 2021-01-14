#include <iostream>
using namespace std;

int main()
{
    int x, y;
    cin >> x >> y;
    bool res = abs(x - y) < 3;
    cout << (res ? "Yes" : "No") << endl;
}
