#include<iostream>
#include<algorithm>

using namespace std;

long long int precos[2001];
long long int memory[2001][2001];
int n;

long long int f(int i, int j){
    if(i>j) return 0;
    int dia = 1 + i + (n-1) - j;
    if(memory[i][j] != -1) return memory[i][j];
    memory[i][j] = max(dia*precos[i]+f(i+1, j), dia*precos[j]+f(i, j-1));
    return memory[i][j];
}


int main(){

    cin >> n;
    for(int i = 0; i < n; i++) cin >> precos[i];
    for(int i = 0; i <= n; i++){
        for(int j = 0; j <= n; j++) memory[i][j] = -1;
    }
    cout << f(0, n-1) << endl;
    return 0;
}