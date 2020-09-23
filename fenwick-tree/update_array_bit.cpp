#include <iostream>
#include <vector>


#define endl '\n'
#define D(x) cout << #x << " = " << (x) << endl;

using namespace std;

typedef vector<int> vi;


class FenwickTree
{
private:
    /* data */
    vi ft;
public:
    FenwickTree(int n)
    {
        ft.assign(n + 1, 0);
    }

    int rsq_util(int b)
    {
        int sum = 0;
        for (; b; b -= b & (-b))
            sum += ft[b];
        return sum;
    }

    void adjust(int k, int v){
        for(;k<(int)ft.size(); k += k&(-k))
            ft[k] += v;
    }
};

int main(){

    int t, n, u, l, r, val, q, q_id;
    cin >> t;

    for(int i = 0; i < t; i++){
        cin >> n >> u;

        FenwickTree fenwick_tree(n);

        for(int j = 0; j < u; j++){
            cin >> l >> r >> val;
            l++;
            r++;

            fenwick_tree.adjust(l, val);
            fenwick_tree.adjust(r+1, -val);
        }

        cin >> q;
        
        for(int j = 0; j < q; j++){
            cin >> q_id;
            q_id++;
            cout << fenwick_tree.rsq_util(q_id) << endl;
        }
    }

    return 0;
}