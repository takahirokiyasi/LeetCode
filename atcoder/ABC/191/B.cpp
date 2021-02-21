#include <bits/stdc++.h>
using namespace std;

int main()
{
    int i, tmp;
    int N, X;
    cin >> N >> X;
    vector<unsigned int> a;
    for (i = 0; i < N; i++)
    {
        cin >> tmp;
        if (tmp != X)
        {
            a.push_back(tmp);
        }
    }
    if (!a.empty())
    {
        for (i = 0; i <= a.size() - 1; i++)
        {
            cout << a.at(i) << " ";
        }
        cout << "\n";
    }
    else
    {
        cout << "\n";
    }
    return 0;
}