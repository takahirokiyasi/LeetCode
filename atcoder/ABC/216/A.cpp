#include <bits/stdc++.h>
using namespace std;

int main()
{
    int X, Y;
    scanf("%d.%d", &X, &Y);

    cout << X;
    if (Y <= 2)
        cout << "-";
    else if (7 <= Y && Y <= 9)
        cout << "+";
    cout << endl;
    return 0;
}
