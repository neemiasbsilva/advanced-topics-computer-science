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

vi c(1000 + 1), v(1000+1);

int t, n;

int pipe_cutting(int d){
    if(d == t) return 0;
    else if(d > t) return INF;
    int result = INF;
    for(int i = 0; i < n; i++){
        result = max(result, v[i] + pipe_cutting(d+c[i]));
    }
    return result;
}

int main(){
    while(cin >> n >> t){
        for(int i = 0; i < n; i++) cin >> c[i] >> v[i];

        cout << pipe_cutting(0);
    }
    return 0;
}