#include <iostream>
#include <vector>
#include <climits>
#include <algorithm>
#include <string.h>

#define INF INT_MIN / 2
#define endl '\n'
#define D(x) cout << #x << " = " << (x) << endl;

using namespace std;

typedef vector<int> vi;

int n;
vi w(1000+1), v(1000+1);

int help_vania(int i, int c){
    if(c >= 0 and i == n) return 0;
    else if(c < 0) return INF;

    return max(help_vania(i+1, c), v[i] + help_vania(i+1, c - w[i]));
}


int main(){

    int c, h;
    h = 0;
    while(true){
        h++;
        cin >> n >> c;
        if(n==0) break;

        for(int i = 0; i < n; i++) cin >> w[i] >> v[i];

        cout << "Caso " << h << ": " << help_vania(0, c) << endl;
    }

    return 0;
}