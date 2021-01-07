#include <iostream>
using namespace std;

int main()
{
    int m, n;
    cin >> m >> n;
    int ans = 0, res = 0;
    while (m)
    {
        ans += m % 10;
        m /= 10;
    }
    while (n)
    {
        res += n % 10;
        n /= 10;
    }
    cout << max(res, ans) << endl;
}