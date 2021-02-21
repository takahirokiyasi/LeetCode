#include <bits/stdc++.h>
using namespace std;

int main()
{
    int V, T, S, D;
    cin >> V >> T >> S >> D;
    cout << ((D < V * T) || (D > V * S) ? "Yes" : "No") << endl;
}