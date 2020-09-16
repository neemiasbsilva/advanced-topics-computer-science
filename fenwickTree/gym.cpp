#include<iostream>
#include<vector>
#include <algorithm>

#define endl '\n'
#define D(x) cout << #x << " = " << (x) << endl;

using namespace std;

typedef vector<int> vi;


class FenwickTree {
    private: 
        vi ft;

    public:

        FenwickTree(int n){
            ft.assign(n+1, 0);
        }

        int rsqUtil(int b){
            int sum = 0;

            for(; b; b -= b&(-b)){
                sum += ft[b];
            }
            return sum;
        }

        int rsq(int a, int b){
            return rsqUtil(b) - (a == 1 ? 0: rsqUtil(a-1));
        }

        void adjust(int k, int v){
            for(; k; k += k&(-k)) ft[k] += v;
        }
};

int main(){
    int ip, m, pc, na, count;

    while(cin >> ip >> m){
        vi l_pc, l_na;

        for (int i = 0; i < m; i++)
        {
            cin >> pc >> na;
            l_pc.push_back(pc);
            l_na.push_back(na);
        }
        int size = *max_element(l_pc.begin(), l_pc.end());

        FenwickTree fenwickTree(size);
        count = 0;
        for (int i = 0; i < size; i++)
        {
            pc = l_pc[i];
            na = l_na[i];

            int pcmax = (pc+ip > size ? size:pc+ip);
            int pcmin = (pc-ip <= 0 ? 1: pc-ip);

            if(fenwickTree.rsq(pcmin, pcmax) <= na) {
                count += 1;
                fenwickTree.adjust(pc, 1);
            }
        }

        cout << count << endl;
        
    }

    return 0;
}