#include <iostream>
#include <vector>

#define endl '\n'
#define lli long long int
#define D(x) cout << #x << " = " << (x) << endl;

using namespace std;

typedef vector<lli> vi;

class FenwickTree{
public:
    vi ft;

    FenwickTree(int n){
        ft.assign(n+1, 0);
    }

    lli rsq_util(int b)
    {
        lli sum = 0;
        for(; b; b-= b&(-b)) sum += ft[b];

        return sum;
    }

    lli rsq(int a, int b)
    {
        if(a == 1) return rsq_util(b);
        
        return rsq_util(b) - rsq_util(a-1);
    }

    void adjust(int k, int v){
        while(k < ft.size()){
            ft[k] += v;
            k += k&(-k);
        }
    }
    
};


int main(){

    int n, q, l_i, r_x;
    lli v;
    char op;
    cin >> n;
    
    FenwickTree fenwick_tree(n);

    for(int i = 0; i < n; i++){
        cin >> v;
        fenwick_tree.adjust(i+1, v);
    }

    cin >> q;

    while(q--){
        cin.ignore();
        cin >> op >> l_i >> r_x;

        if(op == 'q')
            cout << fenwick_tree.rsq(l_i, r_x) << endl;
        else fenwick_tree.adjust(l_i, r_x);
    }
    return 0;
}
