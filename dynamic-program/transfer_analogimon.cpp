#include <iostream>
#include <vector>
#include <climits>
#include <algorithm>
#include <string.h>
#include <math.h>

#define INF INT_MIN / 2
#define endl '\n'
#define D(x) cout << #x << " = " << (x) << endl;

using namespace std;

typedef vector<int> vi;

int n;
vi d((int)pow(10, 4)+1), p((int)pow(10, 4)+1);

int memory[10000+1][10000+1];

int transfer_analogimon(int i, int k)
{
    if(k >= 0 and i == n) return 0;
    else if(k < 0) return INF;

    if(memory[i][k] != -1) return memory[i][k];
    memory[i][k] = max(transfer_analogimon(i + 1, k), d[i] + transfer_analogimon(i + 1, k - p[i]));
    return memory[i][k];
}

int main()
{
    int k;

    while(cin >> n >> k){
        for(int i = 0; i <= n; i++){
            for(int j = 0; j <= k; j++) memory[i][j] = -1;
        }
        for(int i = 0; i < n; i++) cin >> d[i];
        for(int i = 0; i < n; i++) cin >> p[i];

        cout << transfer_analogimon(0, k) << endl;
    }


    return 0;
}