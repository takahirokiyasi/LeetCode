#include <iostream>
using namespace std;
#include <bits/stdc++.h>

int main()
{
    int n;
    cin >> n;
    int x = pow(2, n);
    int half_x = x / 2;
    int before_max = 0;
    int before_index = 0;
    for (int i = 0; i < half_x; i++)
    {
        int a = 0;
        cin >> a;
        if (before_max < a)
        {
            before_max = a;
            before_index = i + 1;
        }
    }
    int after_max = 0;
    int after_index = 0;
    for (int i = half_x; i < x; i++)
    {
        int a = 0;
        cin >> a;
        if (after_max < a)
        {
            after_max = a;
            after_index = i + 1;
        }
    }
    printf("%d", (after_max < before_max)
                     ? after_index
                     : before_index);
}