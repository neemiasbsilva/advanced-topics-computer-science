#include <iostream>
#include <vector>
#include <climits>
#include <algorithm>
#include <string.h>

#define INF INT_MAX/2
#define endl '\n'
#define D(x) cout << #x << " = " << (x) << endl;

using namespace std;

typedef vector<int> vi;

int n;
vi d(1000 + 1), m(1000+1);
int memory[1000 + 1][2000 + 1];

// void prin(int p){
//     for (int i = 0; i <= n; i++)
//     {
//         for (int j = 0; j <= p; j++)
//             cout << memory[i][j] << ' ';
//         cout << endl;
//     }
//     cout << endl;
// }

int amount_mana_dp(int i, int p)
{
    // prin(p);
    if(p <= 0) return 0;
    else if(i == n) return INF;

    if(memory[i][p] != -1) return memory[i][p];

    memory[i][p] = min(amount_mana_dp(i + 1, p), m[i] + amount_mana_dp(i + 1, p - d[i]));
    return memory[i][p];
}

int main()
{

    int p, result;

    while(cin >> n >> p){

        for(int i= 0; i <= n; i++){
            for(int j = 0; j <= p; j++)
                memory[i][j] = -1;
        }


        for(int i = 0; i < n; i++) cin >> d[i] >> m[i];
        
        result = amount_mana_dp(0, p);

        if(result >= INF) cout << "-1" << endl;
        else cout << result << endl;

    }

    return 0;
}