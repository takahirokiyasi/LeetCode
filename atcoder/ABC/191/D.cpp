#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define S second
#define F first
#define FAST                      \
    ios_base::sync_with_stdio(0); \
    cin.tie(0);                   \
    cout.tie(0)
#define vll vector<long long int>
#define pll pair<long long int, long long int>
/* unordered_map<int,int>mp; mp.reserve(1024); mp.max_load_factor(0.25); */
#define mod 1000000007
#define mod2 998244353
#define ll long long int
#define ld long double
#define pi 3.141592653589793238
#define Endl endl
#define endl "\n"
const int N = 5e5 + 5;
const ll inf = 1e18;

void solve()
{
    ld x, y, r;
    cin >> x >> y >> r;
    r += 1e-14;
    ld lll = ceil(y - r), rrr = floor(y + r);
    ll ans = 0;
    for (ld i = lll; i <= rrr; i++)
    {
        ld range = sqrt(r * r - pow(i - y, 2));
        ld left = ceil(x - range);
        ld right = floor(x + range);
        ans += right - left + 1;
    }
    cout << ans;
}

void debug(ll tt) {}

signed main()
{
    FAST;
    int t = 1;
    // cin >> t;
    while (t--)
    {
        solve();
    }
}