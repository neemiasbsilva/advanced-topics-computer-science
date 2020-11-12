#include <iostream>
#include <vector>
#include <climits>
#include <algorithm>

#define INF INT_MAX/2
#define endl '\n'
#define D(x) cout << #x << " = " << (x) << endl;

using namespace std;

typedef vector<int> vi;

int n;
vi d(1000 + 1), m(1000+1);

int amount_mana(int i,int p){
    if(p <= 0) return 0;
    else if(i == n) return INF;

    return min(amount_mana(i+1, p), m[i] + amount_mana(i+1, p-d[i]));
}


int main()
{

    int p, result;

    while(cin >> n >> p){
        for(int i = 0; i < n; i++) cin >> d[i] >> m[i];
        result = amount_mana(0, p);

        if(result >= INF) cout << "-1" << endl;
        else cout << result << endl;

    }

    return 0;
}